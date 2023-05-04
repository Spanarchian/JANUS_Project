from fastapi.testclient import TestClient

from api.janusservice import api

client = TestClient(api)

def test_api_root_extract():
    response = client.get("/cip")
    assert response.status_code == 200
    assert response.json() == {"status": {"Janus extract processor":"Inteligence"}}

def test_api_cip_live():
    response = client.get("/cip/live")
    assert response.status_code == 200
    assert response.json() == {"CIP": "LIVE"}

def test_api_cip_history():
    response = client.get("/cip/history")
    assert response.status_code == 200
    assert response.json() == [{"CIP": "HISTORY"}, {"Status": "Actual display at the time"}]

def test_api_cip_filter():
    response = client.get("/cip/filter")
    assert response.status_code == 200
    assert response.json() == [
        {"CIP": "FILTER"},
        {"Parameters": 'from: strt - till: till'}
    ]