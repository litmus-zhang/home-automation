from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/api/healthchecker")
    assert response.status_code == 200
    assert response.json() == {"message": "System is OK"}


def test_create_user():
    sampleUser = {
        "firstname": "John",
        "lastname": "Doe",
        "email": "johndoe@gmail.com",
    }
    response = client.post("/api/users", json=sampleUser)
    assert response.status_code == 201
    assert response.json()["message"] == "User created successfully"

def test_prevent_duplicate_user():
    sampleUser = {
        "firstname": "John",
        "lastname": "Doe",
        "email": "johndoe@gmail.com",
    }
    response = client.post("/api/users", json=sampleUser)
    assert response.status_code == 400
    assert response.json()["detail"] == "User already exist"



def test_get_all_users():
    response = client.get("/api/users")
    assert response.status_code == 200
    assert len(response.json()) > 0



def test_create_device():
    sampleDevice = {
        "name" : "front Door",
    }
    response = client.post("/api/devices", json=sampleDevice)
    assert response.status_code == 201
    assert response.json()["message"] == "Device created successfully"



