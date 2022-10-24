from kafka import KafkaProducer

from src.config import DEBUG, KAFKA_DSN, KAFKA_PASSWORD, KAFKA_USERNAME

if DEBUG:
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
