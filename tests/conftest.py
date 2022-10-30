import json

import pytest
from kafka import KafkaConsumer, KafkaProducer
from kafka.admin import ConfigResource, KafkaAdminClient
from starlette.testclient import TestClient

from src.app import app
from src.config import KAFKA_DSN, KAFKA_TOPIC

SAMPLE_MESSAGE = {
    "checksum": "e6cd69605e0fa4a46439f2e87ebcc757",
    "client": "a79cefed0b7076cf3998ef7578a18bf0",
    "e": [
        {
            "device_id": "6rPzaVUwYHquzptdsrrKff",
            "user_id": "test_user",
            "timestamp": 1667130434980,
            "event_id": 7,
            "session_id": 1667130434980,
            "event_type": "Dart Click",
            "version_name": None,
            "platform": "Web",
            "os_name": "Chrome",
            "os_version": "106",
            "device_model": "Windows",
            "device_manufacturer": None,
            "language": "en-US",
            "api_properties": {},
            "event_properties": {},
            "user_properties": {},
            "uuid": "52c0306f-f972-45e8-8055-9d05c940e809",
            "library": {"name": "amplitude-flutter", "version": "3.10.0"},
            "sequence_number": 9,
            "groups": {},
            "group_properties": {},
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        }
    ],
    "upload_time": "1667130434980",
    "v": "2",
}


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
        ).encode(
            "utf-8"
        ),
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
    return SAMPLE_MESSAGE


@pytest.fixture(scope="function")
def generate_test_form():
    return SAMPLE_MESSAGE
