package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"strings"
	"sync"
	"time"

	"github.com/confluentinc/confluent-kafka-go/v2/kafka"
	"github.com/gorilla/schema"
	jsoniter "github.com/json-iterator/go"
)

type AmplitudeEvent struct {
	Checksum      string `json:"checksum"    schema:"checksum"`
	Client        string `json:"client"      schema:"client"`
	EventsEncoded string `json:"e"           schema:"e"`
	UploadTime    string `json:"upload_time" schema:"upload_time"`
	Version       string `json:"v"           schema:"v"`
}

type RuntimeCtx struct {
	KafkaProducer *kafka.Producer
	TopicName     string
}

var runtimeCtx *RuntimeCtx

var json = jsoniter.ConfigFastest

func init() {
	kafkaAddress := os.Getenv("KAFKA_DSN")
	if kafkaAddress == "" {
		log.Fatal("KAFKA_DSN environment variable not set")
		os.Exit(1)
	}

	kafkaProducer, err := kafka.NewProducer(&kafka.ConfigMap{"bootstrap.servers": kafkaAddress})
	if err != nil {
		log.Fatal(err)
		os.Exit(1)
	}

	topicName := os.Getenv("KAFKA_TOPIC")
	if topicName == "" {
		topicName = "events"
	}

	runtimeCtx = &RuntimeCtx{
		KafkaProducer: kafkaProducer,
		TopicName:     topicName,
	}
}

func processEvent(event AmplitudeEvent, ipAddress string) error {
	log.Println("Processing event:", event)

	var events []map[string]interface{}
	err := json.Unmarshal([]byte(event.EventsEncoded), &events)
	if err != nil {
		return fmt.Errorf("error unmarshalling JSON 'e': %w", err)
	}

	collectorUploadTime := time.Now().UTC().Format(time.RFC3339)

	var wg sync.WaitGroup

	for _, e := range events {
		wg.Add(1)
		go func(e map[string]interface{}) {
			defer wg.Done()

			e["ip_address"] = ipAddress
			e["collector_upload_time"] = collectorUploadTime

			eStr, err := json.Marshal(e)
			if err != nil {
				log.Println("Error marshalling JSON 'e':", err)
				return
			}

			msg, err := json.Marshal(map[string]interface{}{
				"checksum":    event.Checksum,
				"client":      event.Client,
				"upload_time": event.UploadTime,
				"version":     event.Version,
				"e":           string(eStr),
			})
			if err != nil {
				log.Println("Error marshalling JSON:", err)
				return
			}

			err = runtimeCtx.KafkaProducer.Produce(
				&kafka.Message{
					TopicPartition: kafka.TopicPartition{Topic: &runtimeCtx.TopicName, Partition: kafka.PartitionAny},
					Value:          msg,
					Key:            []byte("1"),
				},
				nil,
			)

			if err != nil {
				log.Println("Error producing message:", err)
			}
		}(e)
	}

	wg.Wait()
	return nil
}

func handleCollect(w http.ResponseWriter, r *http.Request) {
	contentType := r.Header.Get("Content-Type")
	ipAddress := r.Header.Get("x-real-ip")
	if ipAddress == "" {
		ipAddress = strings.Split(r.RemoteAddr, ":")[0]
	}

	if contentType == "application/json" {
		log.Println("Got a JSON request")

		requestBody, err := ioutil.ReadAll(r.Body)
		r.Body.Close()
		if err != nil {
			log.Println("Error reading request body:", err)
			w.WriteHeader(http.StatusInternalServerError)
			return
		}

		go processJSONRequest(requestBody, ipAddress)
		w.WriteHeader(http.StatusOK)
		return
	} else if contentType == "application/x-www-form-urlencoded" {
		log.Println("Got a form request")
		processFormRequest(r, ipAddress)
		w.WriteHeader(http.StatusOK)
		return
	} else {
		log.Println("Got an unknown request")
		w.WriteHeader(http.StatusBadRequest)
		return
	}
}

func processJSONRequest(requestBody []byte, ipAddress string) {
	var event AmplitudeEvent
	if err := json.Unmarshal(requestBody, &event); err != nil {
		log.Println("Error decoding JSON request body:", err)
		return
	}

	if err := processEvent(event, ipAddress); err != nil {
		log.Println("Error processing event:", err)
	}
}

func processFormRequest(r *http.Request, ipAddress string) {
	if err := r.ParseForm(); err != nil {
		log.Println("Error parsing form:", err)
		return
	}

	var event AmplitudeEvent
	decoder := schema.NewDecoder()
	if err := decoder.Decode(&event, r.Form); err != nil {
		log.Println("Error decoding form:", err)
		log.Println("Form:", r.Form)
		return
	}

	if err := processEvent(event, ipAddress); err != nil {
		log.Println("Error processing event:", err)
	}
}

func main() {
	http.HandleFunc("/collect", handleCollect)

	if err := http.ListenAndServe(":8000", nil); err != nil {
		log.Fatal(err)
	}
}
