def test_get_activities_returns_200_and_dict_structure(client):
    # Arrange: client fixture

    # Act
    resp = client.get("/activities")

    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    # Known activity exists and has expected fields
    assert "Chess Club" in data
    activity = data["Chess Club"]
    assert "participants" in activity
    assert "max_participants" in activity
