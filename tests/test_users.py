import pytest

@pytest.mark.asyncio
async def test_get_user_success(async_client):
    response = await async_client.post(
        "/users/register",
        json={
    "name": "Test User",
    "website": "https://example.com",
    "age": 25,
    "role": "user",
    "password": "123456"}

    )

    assert response.status_code == 200

    user_id = response.json()["id"]

    response = await async_client.get(f"/users/{user_id}")

    assert response.status_code == 200
    assert response.json()["name"] == "Test User"

@pytest.mark.asyncio
async def test_get_user_not_found(async_client):
    response = await async_client.get("/users/9999")

    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

@pytest.mark.asyncio
async def test_update_user(async_client):
    # create user
    response = await async_client.post(
        "/users/register",
        json={
    "name": "Test Update User",
    "website": "https://example.com",
    "age": 25,
    "role": "user",
    "password": "123456"
        }
    )

    user_id = response.json()["id"]

    # update
    response = await async_client.put(
        f"/users/{user_id}",
        json={"age": 28}
    )

    assert response.status_code == 200
    assert response.json()["age"] == 28

@pytest.mark.asyncio
async def test_update_user_not_found(async_client):
    response = await async_client.put(
        "/users/999",
        json={"name": "Json"}
    )

    assert response.status_code == 404

@pytest.mark.asyncio
async def test_delete_user(async_client):
    response = await async_client.post(
        "/users/register",
        json={
    "name": "Test User",
    "website": "https://example.com",
    "age": 25,
    "role": "user",
    "password": "123456"}
    )
    user_id = response.json()["id"]

    response = await async_client.delete(f"/users/{user_id}")

    assert response.status_code == 204

@pytest.mark.asyncio
async def test_delete_user_not_found(async_client):
    response = await async_client.delete("/users/999")

    assert response.status_code == 404