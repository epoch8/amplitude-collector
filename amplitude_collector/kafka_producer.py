import logging

from kafka import KafkaAdminClient, KafkaProducer
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError

from .config import (
    CLOUD_ENV,
    KAFKA_DSN,
    KAFKA_PASSWORD,
    KAFKA_USERNAME,
    KAFKA_TOPIC,
    KAFKA_TOPIC_CREATE,
)

logger = logging.getLogger(__name__)


KAFKA_SECURITY_PARAMS = {
    "aws": {"security_protocol": "SSL"},
    "yandex": {
        "security_protocol": "SASL_SSL",
        "sasl_mechanism": "SCRAM-SHA-512",
        "sasl_plain_password": KAFKA_PASSWORD,
        "sasl_plain_username": KAFKA_USERNAME,
        "ssl_cafile": "cert/Yandex/CA.pem",
    },
}

if not KAFKA_TOPIC_CREATE:
    kafka_admin = KafkaAdminClient(
        bootstrap_servers=KAFKA_DSN, **KAFKA_SECURITY_PARAMS.get(CLOUD_ENV, {})
    )
    topic_list = [NewTopic(name=KAFKA_TOPIC, num_partitions=1, replication_factor=1)]
    try:
        kafka_admin.create_topics(new_topics=topic_list, validate_only=False)
    except TopicAlreadyExistsError as e:
        logger.error(str(e))

kafka_producer = KafkaProducer(
    bootstrap_servers=KAFKA_DSN, **KAFKA_SECURITY_PARAMS.get(CLOUD_ENV, {})
)
