from kafka import KafkaProducer

from src.config import KAFKA_DSN, KAFKA_PASSWORD, KAFKA_USE_SSL, KAFKA_USERNAME

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
