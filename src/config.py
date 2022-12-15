import os

KAFKA_DSN = os.environ["KAFKA_DSN"]
KAFKA_USE_SSL = os.environ.get("KAFKA_USE_SSL", "True") == "True"
KAFKA_TOPIC = os.environ.get("KAFKA_TOPIC", "events")
IS_TOPIC_CREATED = os.environ.get("TOPICS_TO_CREATE", "True") == "True"

KAFKA_USERNAME = os.environ.get("KAFKA_USERNAME", "collector")
KAFKA_PASSWORD = os.environ.get("KAFKA_PASSWORD", "")

CLOUD = os.environ.get("CLOUD", "aws")
DEBUG = os.environ.get("DEBUG", "True") == "True"
