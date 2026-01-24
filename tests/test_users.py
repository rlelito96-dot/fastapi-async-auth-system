def test_get_user_success(client):
    response = client.post(
        "/users/register",
        json={"email": "user@test.com", "password": "123456"}

    )

    assert response.status_code == 200

    user_id = response.json()["id"]

    response = client.get(f"/users/{user_id}")

    assert response.status_code == 200
    assert response.json()["email"] == "user@test.com"

def test_get_user_not_found(client):
    response = client.get("/users/9999")

    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

def test_update_user(client):
    # create user
    response = client.post(
        "/users/register",
        json={"email": "old@test.com", "password": "123456"}
    )

    user_id = response.json()["id"]

    # update
    response = client.put(
        f"/users/{user_id}",
        json={"email": "new@test.com"}
    )

    assert response.status_code == 200
    assert response.json()["email"] == "new@test.com"

def test_update_user_not_found(client):
    response = client.put(
        "/users/999",
        json={"email": "x@test.com"}
    )

    assert response.status_code == 404

def test_delete_user(client):
    response = client.post(
        "/users/register",
        json={"email": "delete@test.com", "password": "123456"}
    )
    user_id = response.json()["id"]

    response = client.delete(f"/users/{user_id}")

    assert response.status_code == 204

def test_delete_user_not_found(client):
    response = client.delete("/users/999")

    assert response.status_code == 404