from urllib.parse import quote


def test_signup_success_adds_participant(client):
    # Arrange
    activity = "Chess Club"
    email = "newstudent@example.com"
    pre = client.get("/activities").json()
    assert email not in pre[activity]["participants"]

    # Act
    resp = client.post(f"/activities/{quote(activity)}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 200
    body = resp.json()
    assert "Signed up" in body.get("message", "")
    post = client.get("/activities").json()
    assert email in post[activity]["participants"]


def test_signup_duplicate_returns_400(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"  # pre-seeded in app

    # Act
    resp = client.post(f"/activities/{quote(activity)}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 400
    assert resp.json().get("detail") == "Student already signed up"


def test_signup_activity_not_found_returns_404(client):
    # Arrange
    activity = "No Such Activity"
    email = "who@nowhere.edu"

    # Act
    resp = client.post(f"/activities/{quote(activity)}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 404
    assert resp.json().get("detail") == "Activity not found"
