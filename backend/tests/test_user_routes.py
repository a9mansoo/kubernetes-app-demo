def test_get_user_details_route(setup_test_client):
    client = setup_test_client
    response = client.get("/user/1")
    assert response.status_code == 200
    assert response.json() == {"user": "fakename", "id": 1}
