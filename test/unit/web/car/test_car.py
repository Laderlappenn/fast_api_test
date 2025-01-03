from fastapi.testclient import TestClient
import pytest
from decouple import config

import sys

pythonpath = config('PYTHONPATH')
if pythonpath:
    sys.path.append(pythonpath)  # now import main works
from main import app


# TODO add db hot swap on testing
client = TestClient(app)


@pytest.mark.parametrize("path,expected_status", [
    # good cases
    ("/", 200),
    ("/car", 200),
    ("/car/1", 200),
    # bad cases
    ("/not-found", 404),
    #("/car/", 422),
])
def test_endpoints(path, expected_status):
    response = client.get(path)
    assert response.status_code == expected_status


def test_post_endpoint():
    payload = {
       # "id": 111,
        "name": "Toyota Corolla",
        "fuel": "Petrol",
        "price": "20000",
        "category": "Sedan",
        "link": "https://example.com/toyota-corolla"
    }

    response = client.post("/car", json=payload)
    response_data = response.json()
    assert response_data["name"] == payload["name"]
    assert response_data["fuel"] == payload["fuel"]
    assert response_data["price"] == payload["price"]
    assert response_data["category"] == payload["category"]
    assert response_data["link"] == payload["link"]


def test_patch_endpoint():
    payload = {
       # "id": 111,
        "name": "Toyota Corolla",
        "fuel": "Petrol",
        "price": "20000",
        "category": "Sedan",
        "link": "https://example.com/toyota-corolla"
    }

    response = client.patch("/car/111", json=payload)
    response_data = response.json()
    assert response_data["name"] == payload["name"]
    assert response_data["fuel"] == payload["fuel"]
    assert response_data["price"] == payload["price"]
    assert response_data["category"] == payload["category"]
    assert response_data["link"] == payload["link"]


def test_put_endpoint():
    payload = {
       # "id": 111,
        "name": "camry",
        "fuel": "camry",
        "price": "20000",
        "category": "Sedan",
        "link": "https://example.com/toyota-corolla"
    }

    response = client.put("/car/111", json=payload)
    response_data = response.json()
    assert response_data["name"] == payload["name"]
    assert response_data["fuel"] == payload["fuel"]
    assert response_data["price"] == payload["price"]
    assert response_data["category"] == payload["category"]
    assert response_data["link"] == payload["link"]


def test_delete_endpoint():
    payload = {
       # "id": 111,
        "name": "camry",
        "fuel": "camry",
        "price": "20000",
        "category": "Sedan",
        "link": "https://example.com/toyota-corolla"
    }

    response = client.delete("/car/111")
    # TODO add asserts


