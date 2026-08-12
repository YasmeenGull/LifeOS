from fastapi.testclient import TestClient

from src.api.app import app


client = TestClient(app)


def test_weekly_coach_endpoint():
    response = client.get("/coach/weekly")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert "report" in data
    assert isinstance(data["report"], str)