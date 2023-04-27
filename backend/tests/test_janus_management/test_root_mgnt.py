from fastapi.testclient import TestClient

from api.janusservice import api

client = TestClient(api)

def test_api_root_mngt():
    response = client.get("/mngt")
    assert response.status_code == 200
    assert response.json() == {"status": {"Janus management processor":"Operational"}}