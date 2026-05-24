import pytest
from fastapi.testclient import TestClient

from ..app import create_app, generate_app_config

config = generate_app_config()
app = create_app(config)


@pytest.fixture(scope="session")
def setup_test_client():
    client = TestClient(app)
    yield client
