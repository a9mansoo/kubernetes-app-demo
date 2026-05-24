def test_health_check_ready_route(setup_test_client):
    client = setup_test_client
    response = client.get("/hlth/ready")
    assert response.status_code == 200
    assert response.json() == {"msg": "App is ready"}


def test_health_check_live_route(setup_test_client):
    client = setup_test_client
    response = client.get("/hlth/live")
    assert response.status_code == 200
    assert response.json() == {"msg": "App is live"}
