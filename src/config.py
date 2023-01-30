import os

PROJECT_NAME = os.environ.get("PROJECT_NAME", "")

KAFKA_DSN = os.environ["KAFKA_DSN"]
KAFKA_TOPIC = os.environ.get("KAFKA_TOPIC", "events")
KAFKA_TOPIC_CREATE  = os.environ.get("KAFKA_TOPIC_CREATE ", "True") == "True"

KAFKA_USERNAME = os.environ.get("KAFKA_USERNAME", "collector")
KAFKA_PASSWORD = os.environ.get("KAFKA_PASSWORD", "")

CLOUD_ENV = os.environ.get("CLOUD_ENV", "")
DEBUG = os.environ.get("DEBUG", "True") == "True"
