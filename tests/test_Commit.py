
import pytest, requests
from app.api.models import Commit
from app.api.request import RequestManager
import os

requestManager = RequestManager("teradici", "deploy")
token = os.environ.get('TOKEN', "")
print(token)
if token:
    requestManager.add_authorization(token)

PAGE_LIMIT = 1

@pytest.fixture
def commit():
   
    since = requestManager.parse_date("2019-06-01")
    until = requestManager.parse_date("2020-05-31")
    requestManager.add_date_query_param("since", since)
    requestManager.add_date_query_param("until", until)
    print(requestManager.get_fully_qualified_path())
    response = requestManager.get(PAGE_LIMIT)
    return Commit(**response[0]["commit"])


def test_date_happy_path(commit):
    assert commit.is_date_valid("2019-06-01", "2020-05-31"), "Error with basic validation, check the boolean expression in is_date_valid()"

def test_date_bad_string_is_false(commit):
    assert not commit.is_date_valid("fdsafdsaf", "541523"), "Error with datetime formatting, check the try except in is_date_valid()"

def test_date_is_in_invalid_order_is_false(commit):
    assert not commit.is_date_valid("2020-12-31", "2019-06-01"), "Error with basic validation, check the boolean expression in is_date_valid()"

def test_get_user_before_date_range(commit):
    user = commit.get_user("2001-06-01", "2019-05-31")
    assert not user, "Error with basic validation, check the check the try except in is_date_valid()"

def test_get_user_after_date_range(commit):
    user = commit.get_user("2021-06-01", "2022-05-31")
    assert not user, "Error with basic validation, check the check the try except in is_date_valid()"

def test_get_author_before_date_range(commit):
    user = commit.get_author("2001-06-01", "2019-05-31")
    assert not user, "Error with basic validation, check the check the try except in is_date_valid()"

def test_get_author_after_date_range(commit):
    user = commit.get_author("2021-06-01", "2022-05-31")
    assert not user, "Error with basic validation, check the check the try except in is_date_valid()"





