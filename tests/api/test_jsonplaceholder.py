from utils.api_client import APIClient

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts_should_return_200_and_list_not_empty():
    client = APIClient(BASE_URL)

    response = client.get("/posts")

    assert response.status_code == 200

    body = response.json()
    assert isinstance(body, list)
    assert len(body) > 0


def test_create_post_should_return_201_and_echo_back_data():
    client = APIClient(BASE_URL)

    payload = {
        "title": "QA Testing",
        "body": "This is a test post",
        "userId": 1
    }

    response = client.post("/posts", payload)

    # JSONPlaceholder returns 201 for created resources
    assert response.status_code == 201

    body = response.json()
    assert body["title"] == payload["title"]
    assert body["body"] == payload["body"]
    assert body["userId"] == payload["userId"]
    assert "id" in body   # Fake, but always returned