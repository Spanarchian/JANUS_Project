from fastapi.testclient import TestClient

from api.janusservice import api

client = TestClient(api)

def test_api_root_extract():
    response = client.get("/extract")
    assert response.status_code == 200
    assert response.json() == {"status": {"Janus extract processor":"Operational"}}