import requests

BASE_URL = "http://127.0.0.1:5000"

def test_add_user():
    response = requests.post(f"{BASE_URL}/users", json={"name": "John Doe"})
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"

def test_get_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_delete_user():
    response = requests.delete(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    assert response.json()["message"] == "User deleted"
