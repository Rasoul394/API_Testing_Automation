import requests
import pytest

# The base URL for our test API
BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_users_list_status_code():
    """Verify that the API returns status code 200 (OK) for the users list."""
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200


def test_user_data_contains_required_fields():
    """Check if the first user in the list has a name, email, and username."""
    response = requests.get(f"{BASE_URL}/users")
    users = response.json()

    first_user = users[0]
    assert "name" in first_user
    assert "email" in first_user
    assert "username" in first_user


def test_get_single_user_by_id():
    """Verify that we can fetch a specific user by their ID (e.g., ID 1)."""
    user_id = 1
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    user_data = response.json()

    assert response.status_code == 200
    assert user_data["id"] == user_id
    assert "Leanne Graham" in user_data["name"]