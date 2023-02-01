import json
from uuid import uuid4

import pytest
from kafka import KafkaConsumer, KafkaProducer
from kafka.admin import ConfigResource, KafkaAdminClient
from starlette.testclient import TestClient

from src.app import app
from src.config import KAFKA_DSN, KAFKA_TOPIC
from tests.resources import SAMPLE_MESSAGE, SAMPLE_MESSAGE_THREE_EVENTS


@pytest.fixture(scope="session")
def client():
    client = TestClient(app)
    yield client


@pytest.fixture(scope="session", autouse=True)
def admin_client():
    admin_client = KafkaAdminClient(bootstrap_servers=KAFKA_DSN, client_id="test")
    topic_list = []
    topic_list.append(
        ConfigResource(
            resource_type="TOPIC", name=KAFKA_TOPIC, configs={"retention.ms": "60000"}
        )
    )
    admin_client.alter_configs(topic_list)
    yield


@pytest.fixture(scope="function", autouse=True)
def first_message():
    KafkaProducer(bootstrap_servers=KAFKA_DSN).send(
        topic=KAFKA_TOPIC,
        value=json.dumps(
            {
                "ingest_uuid": "1",
                **SAMPLE_MESSAGE,
            }
        ).encode("utf-8"),
        key=b"1",
    )
    yield


@pytest.fixture(scope="function")
def kafka_consumer():
    consumer = KafkaConsumer(
        KAFKA_TOPIC, bootstrap_servers=KAFKA_DSN, auto_offset_reset="earliest"
    )
    yield consumer


@pytest.fixture(scope="function")
def generate_test_json():
    return {
        "id": str(uuid4()),
        **SAMPLE_MESSAGE,
    }


@pytest.fixture(scope="function")
def generate_test_json_three_events():
    return {
        "id": str(uuid4()),
        **SAMPLE_MESSAGE_THREE_EVENTS,
    }


@pytest.fixture(scope="function")
def generate_test_form():
    return {
        "id": str(uuid4()),
        **SAMPLE_MESSAGE,
    }
