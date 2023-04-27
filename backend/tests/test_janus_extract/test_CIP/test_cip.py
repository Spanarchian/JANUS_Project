from fastapi.testclient import TestClient

from api.janusservice import api

client = TestClient(api)

def test_api_cip_live():
    response = client.get("/extract/cip/live")
    assert response.status_code == 200
    assert response.json() == {"CIP": "LIVE"}

def test_api_cip_history():
    response = client.get("/extract/cip/history")
    assert response.status_code == 200
    assert response.json() == [{"CIP": "HISTORY"}, {"Status": "Actual display at the time"}]

def test_api_cip_filter():
    response = client.get("/extract/cip/filter")
    assert response.status_code == 200
    assert response.json() == [
        {"CIP": "FILTER"},
        {"Parameters": 'from: strt - till: till'}
    ]