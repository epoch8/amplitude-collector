import pytest
from starlette.testclient import TestClient

from src.app import app


@pytest.fixture(scope="session")
def client():
    client = TestClient(app)
    yield client


