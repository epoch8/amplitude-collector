import json

from starlette.testclient import TestClient


def get_data_from_kafka(data: dict, kafka_consumer):
    data_in_kafka = []
    msg_pack = kafka_consumer.poll(timeout_ms=1000)
    for tp, messages in msg_pack.items():
        for msg in messages:
            data_in_kafka.append(json.loads(msg.value))
    for msgs in data_in_kafka:
        if msgs.get("id") == data["id"]:
            return msgs


def assert_kafka_msg_eq(kafka_msg, msg):
    assert kafka_msg["e"] == json.loads(msg["e"])


def test_collect_json(client: TestClient, kafka_consumer, generate_test_json):
    client.headers = {"content-type": "application/json"}  # type: ignore
    response = client.post("/collect", json=generate_test_json)
    assert response.status_code == 200
    assert_kafka_msg_eq(get_data_from_kafka(generate_test_json, kafka_consumer), generate_test_json)


def test_collect_form_data(client: TestClient, kafka_consumer, generate_test_form):
    client.headers = {"content-type": "application/x-www-form-urlencoded"}  # type: ignore
    response = client.post("/collect", data=generate_test_form)
    assert response.status_code == 200
    assert_kafka_msg_eq(get_data_from_kafka(generate_test_form, kafka_consumer), generate_test_form)


def test_collect_unexpected_content_type(client: TestClient):
    client.headers = {"content-type": "unexpected_content_type"}  # type: ignore
    data = {"key1": 1, "key2": "2", "key3": "test"}
    response = client.post("/collect", data=data)
    assert response.status_code == 400
