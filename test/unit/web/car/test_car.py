from fastapi.testclient import TestClient
import pytest


from main import app


client = TestClient(app)


@pytest.mark.parametrize("path,expected_status", [
    # good cases
    ("/", 200),
    ("/car/", 200),
    ("/car/Volkswagen ID.3", 200),
    # bad cases
    ("/not-found", 404)
])
def test_endpoints(path, expected_status):
    response = client.get(path)
    assert response.status_code == expected_status



