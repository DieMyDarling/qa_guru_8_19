import requests
from requests import Response
import jsonschema
from utils import load_schema


def test_get_single_user_200():
    url = "https://reqres.in/api/users/2"
    result: Response = requests.get(url)
    assert result.status_code == 200


def test_get_user_not_found_404():
    url = "https://reqres.in/api/users/23"
    result: Response = requests.get(url)
    assert result.status_code == 404
    assert result.json() == {}


def test_get_all_users_200():
    url = f"https://reqres.in/api/users/"
    result: Response = requests.get(url)
    assert result.status_code == 200
    assert result.json()["total"] == 12
    schema = load_schema("json_schemas/get_all_users_successfully.json")
    jsonschema.validate(result.json(), schema)


def test_create_user_201():
    name = "Pavel"
    job = "leader"
    url = "https://reqres.in/api/users"
    result: Response = requests.post(url, json={'name': f"{name}", 'job': f"{job}"''})
    assert result.status_code == 201
    assert result.json()["name"] == name
    assert result.json()["job"] == job


def test_post_login_200():
    url = "https://reqres.in/api/login"
    result: Response = requests.post(url, json={"email": "eve.holt@reqres.in", "password": "cityslicka"})
    assert result.status_code == 200
    schema = load_schema("json_schemas/post_login_successfully.json")
    jsonschema.validate(result.json(), schema)


def test_post_login_user_not_found_400():
    url = "https://reqres.in/api/login"
    result: Response = requests.post(url, json={"email": "eve", "password": "city"})
    assert result.status_code == 400
    assert result.json() == {"error": "user not found"}


def test_put_update_user_200():
    url = "https://reqres.in/api/users/2"
    result: Response = requests.put(url, json={
        "name": "morpheus",
        "job": "zion resident"
    })
    assert result.status_code == 200
    schema = load_schema("json_schemas/put_update_user_successfully.json")
    jsonschema.validate(result.json(), schema)


def test_patch_user_name_200():
    url = "https://reqres.in/api/books/6"
    result: Response = requests.patch(url, json={"name": "Yura"})
    assert result.status_code == 200
    schema = load_schema("json_schemas/patch_user_name_successfully.json")
    jsonschema.validate(result.json(), schema)


def test_delete_user_200():
    url = f"https://reqres.in/api/users/2"
    result: Response = requests.delete(url)
    assert result.status_code == 204
    assert result.text == ""
