from uuid import uuid4

import pytest
from starlette.testclient import TestClient
from kafka.admin import KafkaAdminClient, ConfigResource
from kafka import KafkaConsumer

from src.app import app
from src.config import KAFKA_TOPIC, KAFKA_DSN


@pytest.fixture(scope="session")
def client():
    client = TestClient(app)
    yield client


@pytest.fixture(scope="session", autouse=True)
def admin_client():
    admin_client = KafkaAdminClient(
        bootstrap_servers=KAFKA_DSN,
        client_id='test'
    )
    topic_list = []
    topic_list.append(ConfigResource(
        resource_type='TOPIC', name=KAFKA_TOPIC, configs={"retention.ms": "60000"})
    )
    admin_client.alter_configs(topic_list)
    yield


@pytest.fixture(scope="function")
def kafka_consumer():
    consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_DSN, auto_offset_reset='earliest')
    yield consumer


@pytest.fixture(scope="function")
def generate_test_json():
    return {"id": str(uuid4()), "key": "test", "key2": 1}


@pytest.fixture(scope="function")
def generate_test_form():
    return {"id": str(uuid4()), "key": "test", "key2": "1"}
