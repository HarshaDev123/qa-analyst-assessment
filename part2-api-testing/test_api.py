"""
Part 2: Basic API Testing — JSONPlaceholder

Uses pytest and the requests library to test three core scenarios against
the JSONPlaceholder REST API (https://jsonplaceholder.typicode.com).

Test cases:
    1. GET  /users/1   — Fetch a user and validate response structure.
    2. POST /posts     — Create a new post and verify the response.
    3. GET  /users/999 — Confirm 404 handling for a non-existent resource.
"""

import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"


# ---------------------------------------------------------------------------
# Test 1: GET request — Fetch a user and validate response structure
# ---------------------------------------------------------------------------

class TestGetUser:
    """Verify that fetching an existing user returns correct status and data."""

    def test_fetch_user_returns_200(self):
        """GET /users/1 should respond with a 200 status code."""
        response = requests.get(f"{BASE_URL}/users/1")
        assert response.status_code == 200

    def test_fetch_user_has_required_fields(self):
        """The response body must include id, name, and email fields."""
        response = requests.get(f"{BASE_URL}/users/1")
        data = response.json()

        assert "id" in data, "Response is missing 'id' field"
        assert "name" in data, "Response is missing 'name' field"
        assert "email" in data, "Response is missing 'email' field"

    def test_fetch_user_returns_correct_id(self):
        """The returned user id should match the requested id."""
        response = requests.get(f"{BASE_URL}/users/1")
        data = response.json()

        assert data["id"] == 1

    def test_fetch_user_email_format(self):
        """The email field should contain a valid '@' symbol."""
        response = requests.get(f"{BASE_URL}/users/1")
        data = response.json()

        assert "@" in data["email"], "Email does not contain '@' symbol"

    def test_response_content_type_is_json(self):
        """The Content-Type header should indicate JSON."""
        response = requests.get(f"{BASE_URL}/users/1")

        assert "application/json" in response.headers.get("Content-Type", "")


# ---------------------------------------------------------------------------
# Test 2: POST request — Create a new post and verify creation
# ---------------------------------------------------------------------------

class TestCreatePost:
    """Verify that creating a new post returns the expected response."""

    PAYLOAD = {
        "title": "Test Post Title",
        "body": "This is the body of the test post.",
        "userId": 1,
    }

    def test_create_post_returns_201(self):
        """POST /posts should respond with a 201 Created status code."""
        response = requests.post(f"{BASE_URL}/posts", json=self.PAYLOAD)
        assert response.status_code == 201

    def test_create_post_echoes_submitted_data(self):
        """The response should echo back the title, body, and userId we sent."""
        response = requests.post(f"{BASE_URL}/posts", json=self.PAYLOAD)
        data = response.json()

        assert data["title"] == self.PAYLOAD["title"]
        assert data["body"] == self.PAYLOAD["body"]
        assert data["userId"] == self.PAYLOAD["userId"]

    def test_create_post_assigns_id(self):
        """The API should assign an id to the newly created post."""
        response = requests.post(f"{BASE_URL}/posts", json=self.PAYLOAD)
        data = response.json()

        assert "id" in data, "Response is missing 'id' for the new post"
        assert isinstance(data["id"], int)

    def test_create_post_with_empty_body(self):
        """POST /posts with an empty payload should still return 201."""
        response = requests.post(f"{BASE_URL}/posts", json={})
        assert response.status_code == 201


# ---------------------------------------------------------------------------
# Test 3: Error handling — 404 for a non-existent resource
# ---------------------------------------------------------------------------

class TestNotFound:
    """Verify the API responds correctly for non-existent resources."""

    def test_nonexistent_user_returns_404(self):
        """GET /users/999 should respond with a 404 Not Found status code."""
        response = requests.get(f"{BASE_URL}/users/999")
        assert response.status_code == 404

    def test_nonexistent_user_returns_empty_body(self):
        """The response body for a missing resource should be empty or {}."""
        response = requests.get(f"{BASE_URL}/users/999")
        data = response.json()

        # JSONPlaceholder returns an empty object for missing resources
        assert data == {} or data == []

    def test_nonexistent_post_returns_404(self):
        """GET /posts/99999 should also return a 404 status code."""
        response = requests.get(f"{BASE_URL}/posts/99999")
        assert response.status_code == 404
