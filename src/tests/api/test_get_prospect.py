from tests.fixtures.user import user


def test_get_prospect_all(client):
    client.post("/lead/", json=user)
    response = client.get("/prospect/")
    assert response.status_code == 200
    assert type(response.json()) == list


def test_get_prospect_per_id(client):
    client.post("/lead/", json=user)
    response = client.get(f"/prospect/{user['identification_number']}")
    assert response.status_code == 200
    assert type(response.json()) == list
