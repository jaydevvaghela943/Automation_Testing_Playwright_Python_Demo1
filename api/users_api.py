from api.api_client import APIClient


client = APIClient()


def get_users():

    return client.get(
        "https://reqres.in/api/users"
    )