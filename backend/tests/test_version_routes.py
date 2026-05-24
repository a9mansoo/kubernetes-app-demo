def test_get_app_version_info(setup_test_client):
    client = setup_test_client
    response = client.get("/info/version")
    assert response.status_code == 200
    assert response.json() == {"version": "dev"}
