from api.api_client import APIClient

client = APIClient()


def login_api():

    payload = {
        "email": "admin@test.com",
        "password": "123456"
    }

    response = client.post(
        "https://reqres.in/api/login",
        payload
    )

    return response