# Configuration

## ENV vars

* `CLOUD` - cloud service in which the application runs
* `DEBUG` - `True`/`False` - echo incoming messages to stdout

* `KAFKA_DSN` - hostname of kafka cluster
* `KAFKA_USE_SSL` - `True`/`False` - whether to use SSL and cert checking to
  connect to Kafka cluster (required in Yandex Cloud)
* `KAFKA_USERNAME`
* `KAFKA_PASSWORD`

* `KAFKA_TOPIC` - topic name to write
* `KAFKA_TOPIC_CREATE ` - is the topic created? if False, it will be created automatically
