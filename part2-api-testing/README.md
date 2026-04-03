# Part 2: Basic API Testing — JSONPlaceholder

## Overview

Automated tests covering core REST API scenarios against the JSONPlaceholder fake API:

| # | Scenario | Endpoint | Key Assertions |
|---|----------|----------|----------------|
| 1 | **GET request** | GET /users/1 | 200 status, required fields (id, name, email), correct id, email format, JSON content type |
| 2 | **POST request** | POST /posts | 201 status, echoed payload, assigned id, empty-body edge case |
| 3 | **Error handling** | GET /users/999 | 404 status, empty response body, also tests non-existent post |

## How to Run

pip install -r requirements.txt
pytest test_api.py -v

## Expected Output

test_api.py::TestGetUser::test_fetch_user_returns_200              PASSED
test_api.py::TestGetUser::test_fetch_user_has_required_fields      PASSED
test_api.py::TestGetUser::test_fetch_user_returns_correct_id       PASSED
test_api.py::TestGetUser::test_fetch_user_email_format             PASSED
test_api.py::TestGetUser::test_response_content_type_is_json       PASSED
test_api.py::TestCreatePost::test_create_post_returns_201          PASSED
test_api.py::TestCreatePost::test_create_post_echoes_submitted_data PASSED
test_api.py::TestCreatePost::test_create_post_assigns_id           PASSED
test_api.py::TestCreatePost::test_create_post_with_empty_body      PASSED
test_api.py::TestNotFound::test_nonexistent_user_returns_404       PASSED
test_api.py::TestNotFound::test_nonexistent_user_returns_empty_body PASSED
test_api.py::TestNotFound::test_nonexistent_post_returns_404       PASSED

## Note
The test suite follows the assignment prompt for missing-resource behavior. Because JSONPlaceholder is a public fake API, missing-resource responses may vary at runtime.

