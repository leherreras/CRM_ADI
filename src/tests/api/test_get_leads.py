import names

user = {
    "identification_number": "123456789",
    "first_name": names.get_first_name(),
    "last_name": names.get_last_name(),
    "email": "test@test.com",
    "birthdate": "01/01/2000"
}


def test_get_leads_0(client):
    response = client.get("/lead/count")
    assert response.status_code == 200
    assert response.json() == 0


def test_get_leads_1(client):
    client.post("/lead/", json=user)
    response = client.get("/lead/count")
    assert response.status_code == 200
    assert response.json() == 1


def test_get_leads_10(client):
    for i in range(1, 10):
        client.post("/lead/", json=user)
    response = client.get("/lead/count")
    assert response.status_code == 200
    assert response.json() == 10
