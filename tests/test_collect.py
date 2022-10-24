from starlette.testclient import TestClient


def test_collect_json(client: TestClient):
    client.headers = {"content-type": "application/json"}
    data = {"key1": 1, "key2": "2", "key3": "test"}
    response = client.post("/collect", json=data)
    assert response.status_code == 200


def test_collect_form_data(client: TestClient):
    client.headers = {"content-type": "application/x-www-form-urlencoded"}
    data = {"key1": 1, "key2": "2", "key3": "test"}
    response = client.post("/collect", data=data)
    assert response.status_code == 200


def test_collect_unexpected_content_type(client: TestClient):
    client.headers = {"content-type": "unexpected_content_type"}
    data = {"key1": 1, "key2": "2", "key3": "test"}
    response = client.post("/collect", data=data)
    assert response.status_code == 400
