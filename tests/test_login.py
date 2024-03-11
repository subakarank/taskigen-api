from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_login():
    response = client.get("/login")
    assert response.status_code == 200
    assert response.json() == {"message": "This is login page"}
