from tests.fixtures.user import user


def test_post_lead(client):
    response = client.post("/lead/", json=user)
    assert response.status_code == 200
