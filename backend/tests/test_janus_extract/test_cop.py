from fastapi.testclient import TestClient

from api.janusservice import api

client = TestClient(api)

def test_api_root_extract():
    response = client.get("/cop")
    assert response.status_code == 200
    assert response.json() == {"status": {"Janus extract processor":"Operational"}}

def test_api_cop_live():
    response = client.get("/cop/live")
    assert response.status_code == 200
    assert response.json() == {"cop": "LIVE"}

def test_api_cop_history():
    response = client.get("/cop/history")
    assert response.status_code == 200
    assert response.json() == [{"cop": "HISTORY"}, {"Status": "Actual display at the time"}]

def test_api_cop_filter():
    response = client.get("/cop/filter")
    assert response.status_code == 200
    assert response.json() == [
        {"cop": "FILTER"},
        {"Parameters": 'from: strt - till: till'}
    ]
