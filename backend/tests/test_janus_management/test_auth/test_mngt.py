from fastapi.testclient import TestClient

from api.janusservice import api

client = TestClient(api)


def test_api_mngt_login():
    response = client.get("/mngt/login")
    assert response.status_code == 200
    assert response.json() == {"status": "User has logged in"}

def test_api_mngt_logout():
    response = client.get("/mngt/logout")
    assert response.status_code == 200
    assert response.json() == {"status": "User has logged out"}

def test_api_mngt_forgot():
    response = client.get("/mngt/forgot")
    assert response.status_code == 200
    assert response.json() == {"status": "Password reset details have been sent to your listed Email."}