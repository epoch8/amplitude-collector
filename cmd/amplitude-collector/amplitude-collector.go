package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
	"strings"
	"time"

	"gopkg.in/confluentinc/confluent-kafka-go.v1/kafka"
)

type AmplitudeEvent struct {
	Checksum      string `json:"checksum"`
	Client        string `json:"client"`
	EventsEncoded string `json:"e"`
	UploadTime    string `json:"upload_time"`
	Version       string `json:"v"`
}

type RuntimeCtx struct {
	KafkaProducer *kafka.Producer
	TopicName     string
}

var runtimeCtx *RuntimeCtx

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

	for _, e := range events {
		e["ip_address"] = ipAddress
		e["collector_upload_time"] = collectorUploadTime

		eStr, err := json.Marshal(e)
		if err != nil {
			return fmt.Errorf("error marshalling JSON 'e': %w", err)
		}

		msg, err := json.Marshal(
			map[string]interface{}{
				"checksum":    event.Checksum,
				"client":      event.Client,
				"upload_time": event.UploadTime,
				"version":     event.Version,
				"e":           string(eStr),
			},
		)
		if err != nil {
			return fmt.Errorf("error marshalling JSON: %w", err)
		}

		log.Println("Producing message:", string(msg))

		err = runtimeCtx.KafkaProducer.Produce(
			&kafka.Message{
				TopicPartition: kafka.TopicPartition{Topic: &runtimeCtx.TopicName, Partition: kafka.PartitionAny},
				Value:          msg,
				Key:            []byte("1"),
			},
			nil,
		)
		if err != nil {
			return fmt.Errorf("error producing message: %w", err)
		}
	}

	runtimeCtx.KafkaProducer.Flush(10)

	return nil
}

func handleCollect(w http.ResponseWriter, r *http.Request) {
	ipAddress := r.Header.Get("x-real-ip")
	if ipAddress == "" {
		ipAddress = strings.Split(r.RemoteAddr, ":")[0]
	}

	if r.Header.Get("Content-Type") == "application/json" {
		log.Println("Got a JSON request")

		// Read the request body and unmarshal it into an AmplitudeEvent
		var event AmplitudeEvent
		if err := json.NewDecoder(r.Body).Decode(&event); err != nil {
			log.Println("Error decoding JSON request body:", err)
			w.WriteHeader(http.StatusBadRequest)
			return
		}

		// Process the event
		if err := processEvent(event, ipAddress); err != nil {
			log.Println("Error processing event:", err)
			w.WriteHeader(http.StatusInternalServerError)
		}

		return
		// } else if r.Header.Get("Content-Type") == "application/x-www-form-urlencoded" {
		// 	log.Println("Got a form request")
		// 	return
	} else {
		log.Println("Got an unknown request")
		w.WriteHeader(http.StatusBadRequest)
		return
	}
}

func main() {
	http.HandleFunc("/collect", handleCollect)

	if err := http.ListenAndServe(":8000", nil); err != nil {
		log.Fatal(err)
	}
}
