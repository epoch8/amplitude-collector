import os
import json
from uuid import uuid4
import orjson

import pytest
from kafka import KafkaConsumer, KafkaProducer
from kafka.admin import ConfigResource, KafkaAdminClient

from amplitude_collector.config import KAFKA_DSN, KAFKA_TOPIC
from tests.resources import (
    SAMPLE_MESSAGE,
    SAMPLE_MESSAGE_LOTS_OF_EVENTS,
    SAMPLE_MESSAGE_THREE_EVENTS,
)


@pytest.fixture(scope="session")
def client():
    if (test_endpoint := os.environ.get("TEST_API_ENDPOINT", None)) is not None:
        import httpx

        client = httpx.Client(base_url=test_endpoint)

        yield client

        client.close()
    else:
        from starlette.testclient import TestClient
        from amplitude_collector.app import app

        with TestClient(app) as client:
            yield client

        client.close()


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
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_DSN,
        # auto_offset_reset="earliest",
    )
    consumer.poll(timeout_ms=100)
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
def generate_test_json_lots_of_events():
    return orjson.dumps(
        {
            "id": str(uuid4()),
            **SAMPLE_MESSAGE_LOTS_OF_EVENTS,
        }
    )


@pytest.fixture(scope="function")
def generate_test_form():
    return {
        "id": str(uuid4()),
        **SAMPLE_MESSAGE,
    }
