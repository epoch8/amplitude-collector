import json
import re
import datetime
from starlette.testclient import TestClient


def get_data_from_kafka(data: dict, kafka_consumer):
    data_in_kafka = []
    msg_pack = kafka_consumer.poll(timeout_ms=1000)
    for tp, messages in msg_pack.items():
        for msg in messages:
            msg_dict = json.loads(msg.value)
            data_in_kafka.append(msg_dict)
    for msgs in data_in_kafka:
        if msgs.get("client") == data["client"]:
            return msgs


def get_messages_count_from_kafka(kafka_consumer):
    data_in_kafka = []
    msg_pack = kafka_consumer.poll(timeout_ms=1000)
    for tp, messages in msg_pack.items():
        for msg in messages:
            data_in_kafka.append(json.loads(msg.value))
    return len(data_in_kafka)


def assert_kafka_msg_eq(kafka_msg, msg):
    e = json.loads(kafka_msg["e"])
    e.pop("ip_address")
    e.pop("collector_upload_time")

    assert e == json.loads(msg["e"])[0]


def test_collect_json(client: TestClient, kafka_consumer, generate_test_json):
    client.headers = {"content-type": "application/json"}  # type: ignore
    response = client.post("/collect", json=generate_test_json)
    assert response.status_code == 200
    assert_kafka_msg_eq(
        get_data_from_kafka(generate_test_json, kafka_consumer), generate_test_json
    )


def test_collect_form_data(client: TestClient, kafka_consumer, generate_test_form):
    client.headers = {"content-type": "application/x-www-form-urlencoded"}  # type: ignore
    response = client.post("/collect", data=generate_test_form)
    assert response.status_code == 200
    assert_kafka_msg_eq(
        get_data_from_kafka(generate_test_form, kafka_consumer), generate_test_form
    )


def test_collect_unexpected_content_type(client: TestClient):
    client.headers = {"content-type": "unexpected_content_type"}  # type: ignore
    data = {"key1": "1", "key2": "2", "key3": "test"}
    response = client.post("/collect", data=data)
    assert response.status_code == 400


def test_multiple_events_generate_multiple_records(
    client: TestClient, kafka_consumer, generate_test_json_three_events
):
    client.headers = {"content-type": "application/json"}  # type: ignore
    response = client.post("/collect", json=generate_test_json_three_events)
    assert response.status_code == 200
    second_poll = get_messages_count_from_kafka(kafka_consumer)
    assert second_poll == 3


def test_ip_address_in_message(client: TestClient, kafka_consumer, generate_test_json):
    client.headers = {"content-type": "application/json"}  # type: ignore
    response = client.post("/collect", json=generate_test_json)
    assert response.status_code == 200
    kafka_msg = get_data_from_kafka(generate_test_json, kafka_consumer)
    e = json.loads(kafka_msg["e"])

    # assert e["ip_address"] matches regex of a valid ip address
    assert (
        re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", e["ip_address"]) is not None
        or e["ip_address"] == "testclient"
    )


def test_server_timestamp_in_message(
    client: TestClient, kafka_consumer, generate_test_json
):
    client.headers = {"content-type": "application/json"}  # type: ignore
    response = client.post("/collect", json=generate_test_json)
    assert response.status_code == 200
    kafka_msg = get_data_from_kafka(generate_test_json, kafka_consumer)
    e = json.loads(kafka_msg["e"])

    time_diff = datetime.datetime.now(
        datetime.timezone.utc
    ) - datetime.datetime.fromisoformat(e["collector_upload_time"])

    assert time_diff < datetime.timedelta(seconds=1)
