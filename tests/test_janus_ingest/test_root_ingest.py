from fastapi.testclient import TestClient

from api.janusservice import api

client = TestClient(api)

def test_api_root1():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": {"Janus Core":"Operational"}}