from fastapi.testclient import TestClient

from api.janusservice import api

client = TestClient(api)

def test_api_user_listing():
    response = client.get("/users/all")
    assert response.status_code == 200
    assert response.json() == {
    "u0001" : {"ref": "u0001", "role": "admin", "uname": "Spanarchian", "email":"spanarchian@gmail.com", "loc":"Wales", "pword" : "Pas55word!"},
    "u0002" : {"ref": "u0002", "role": "moderator", "uname": "SouthCoastpy", "email":"southcoastpy@gmail.com", "loc":"England", "pword" : "Pas55word!"},
    "u0003" : {"ref": "u0003", "role": "user", "uname": "Itestedthis1", "email":"itestedthis1@gmail.com", "loc":"Scotland", "pword" : "Pas55word!"},
    "u0004" : {"ref": "u0004", "role": "user", "uname": "QuantumOfHope", "email":"aquantumofhope@gmail.com", "loc":"Ireland", "pword" : "Pas55word!"}
}


def test_api_user_current():
    response = client.get("/users/me")
    assert response.status_code == 200
    assert response.json() == {
"ref": "u0001",
"role": "admin",
"uname": "Spanarchian",
"email": "spanarchian@gmail.com",
"loc": "Wales",
"pword": "Pas55word!"}