from fastapi.testclient import TestClient

from src.api.app import app


client = TestClient(app)


def test_home():

    response = client.get("/")

    assert response.status_code == 200


def test_score():

    response = client.get("/score")

    assert response.status_code == 200

    assert "discipline_score" in response.json()