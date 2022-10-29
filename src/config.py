import os

from kafka import KafkaProducer

KAFKA_DSN = os.environ["KAFKA_DSN"]
KAFKA_USE_SSL = os.environ.get("KAFKA_USE_SSL", "True") == "True"
KAFKA_TOPIC = os.environ.get("KAFKA_TOPIC", "events")

KAFKA_USERNAME = os.environ.get("KAFKA_USERNAME", "collector")
KAFKA_PASSWORD = os.environ.get("KAFKA_PASSWORD", "")

DEBUG = os.environ.get("DEBUG", "True") == "True"

if not KAFKA_USE_SSL:
    kafka_producer = KafkaProducer(bootstrap_servers=KAFKA_DSN)
else:
    kafka_producer = KafkaProducer(
        bootstrap_servers=KAFKA_DSN,
        security_protocol="SASL_SSL",
        sasl_mechanism="SCRAM-SHA-512",
        sasl_plain_password=KAFKA_PASSWORD,
        sasl_plain_username=KAFKA_USERNAME,
        ssl_cafile="cert/Yandex/CA.pem",
    )
