
import pytest, requests
from app.api.repository import CommitRepository
from app.api.request import RequestManager
import os


requestManager = RequestManager("teradici", "deploy")
token = os.environ.get('TOKEN', "")
print(token)
if token:
    requestManager.add_authorization(token)

PAGE_LIMIT = 1

@pytest.fixture
def response():
    since = requestManager.parse_date("2019-06-01")
    until = requestManager.parse_date("2020-05-31")
    requestManager.add_date_query_param("since", since)
    requestManager.add_date_query_param("until", until)
    print(requestManager.get_fully_qualified_path())
    return requestManager.get(PAGE_LIMIT)


def test_get_users(response):
    commitRepository = CommitRepository()
    users = commitRepository.get_users(response, "2019-06-01", "2020-05-31")
    assert users[0], "Error with response to model mapping, check response structure and kwargs mapping"


def test_get_frequent_committers(response):
    commitRepository = CommitRepository()
    authors = commitRepository.get_authors(response, "2019-06-01", "2020-05-31")
    frequentCommitters = commitRepository.get_frequent_committers_as_list(authors)
    assert frequentCommitters[0], "Error with response to model mapping, check response structure and kwargs mapping"