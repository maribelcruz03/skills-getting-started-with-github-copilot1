from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_get_activities_returns_data():
    response = client.get("/activities")

    assert response.status_code == 200
    assert "Chess Club" in response.json()


def test_cannot_register_same_student_twice_for_same_activity():
    email = "michael@mergington.edu"

    response = client.post(f"/activities/Chess Club/signup?email={email}")

    assert response.status_code == 400
    assert response.json()["detail"] == "Student is already signed up"
