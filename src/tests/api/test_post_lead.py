import names

user = {
    "identification_number": "123456789",
    "first_name": names.get_first_name(),
    "last_name": names.get_last_name(),
    "email": "test@test.com",
    "birthdate": "01/01/2000"
}


def test_post_lead(client):
    response = client.post("/lead/", json=user)
    assert response.status_code == 200
