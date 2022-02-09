from app import create_app, cache
from app.api.routes import is_query_params_valid
import pytest, requests


@pytest.fixture(scope='session')
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

###Get User
def test_users_Happy_Path(client):
    users = client.get('/users?start=2019-06-01&end=2020-05-31')
    assert users.status_code == 200, "Successful response failed, check routes.py for misconfiguration"

def test_users_400_missing_query_params(client):
    users = client.get('/users')
    assert users.status_code == 400, "Error in query parameter validation, check routes.py is_query_params_valid"

def test_users_400_invalid_query_params(client):
    users = client.get('/users?start=fdasfdsfasdf1&end=223423')
    assert users.status_code == 400, "Error in query parameter validation, check routes.py is_query_params_valid"


def test_users_400_start_after_end(client):
    users = client.get('/users?start=2020-05-31&end=2019-06-01')
    assert users.status_code == 400, "Error in query parameter validation, check routes.py is_query_params_valid"


###Get Most Frequent
def test_most_frequent_Happy_Path(client):
    users = client.get('/most-frequent?start=2019-06-01&end=2020-05-31')
    assert users.status_code == 200, "Successful response failed, check routes.py for misconfiguration"
   
def test_most_frequent_400_missing_query_params(client):
    users = client.get('/most-frequent')
    assert users.status_code == 400, "Error in query parameter validation, check routes.py is_query_params_valid"

def test_most_frequent_400_invalid_query_params(client):
    users = client.get('/most-frequent?start=fdasfdsfasdf1&end=223423')
    assert users.status_code == 400, "Error in query parameter validation, check routes.py is_query_params_valid"


def test_most_frequent_400_start_after_end(client):
    users = client.get('/most-frequent?start=2020-05-31&end=2019-06-01')
    assert users.status_code == 400, "Error in query parameter validation, check routes.py is_query_params_valid"

###Mock Server
def test_github_200():
    response = requests.get("https://b7af59a4-73d0-46e0-b560-8989895c0baf.mock.pstmn.io/repos/teradici/deploy/commits?page=1")
    response.status_code == 200

def test_github_500():
    response = requests.get("https://b7af59a4-73d0-46e0-b560-8989895c0baf.mock.pstmn.io/repos/teradici/deploy/commits")
    response.status_code == 500