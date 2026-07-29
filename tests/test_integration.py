from fastapi.testclient import TestClient

from src.api.app import app

client = TestClient(app)


def test_log_and_score():

    # Create a log
    response = client.post(
        "/log",
        json={
            "activity": "VS Code",
            "duration": 120,
            "category": "Study"
        }
    )

    assert response.status_code == 200

    # Get discipline score
    response = client.get("/score")

    assert response.status_code == 200

    assert "discipline_score" in response.json()