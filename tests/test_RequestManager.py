import app
from app.api.request import RequestManager



def test_path_with_no_parameters():
    requestManager = RequestManager("teradici", "deploy")
    assert requestManager.get_fully_qualified_path() == "https://api.github.com/repos/teradici/deploy/commits"


def test_path_with_one_param():
    requestManager = RequestManager("teradici", "deploy")
    requestManager.add_query_param("page", 1)
    print(requestManager.get_fully_qualified_path() )
    assert requestManager.get_fully_qualified_path() == "https://api.github.com/repos/teradici/deploy/commits?page=1"

def test_path_with_more_than_one_param():
    requestManager = RequestManager("teradici", "deploy")
    requestManager.add_query_param("page", 1)
    requestManager.add_query_param("per_page", 100)
    print(requestManager.get_fully_qualified_path() )
    assert requestManager.get_fully_qualified_path() == "https://api.github.com/repos/teradici/deploy/commits?page=1&per_page=100"


def test_get_all_pages():
    requestManager = RequestManager("teradici", "deploy")
    requestManager.add_query_param("page", 1)
    requestManager.add_query_param("per_page", 100)
    requestManager.add_authorization("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")
    since = requestManager.parse_date("2019-06-01")
    until = requestManager.parse_date("2020-05-31")
    requestManager.add_date_query_param("since", since)
    requestManager.add_date_query_param("until", until)
    commits = requestManager.get(10)
    assert len(commits) >= 846


def test_date_parser_returns_date():
    requestManager = RequestManager("teradici", "deploy")
    date = requestManager.parse_date("2022-2-7")
    requestManager.add_date_query_param("since", date)
    print(requestManager.get_fully_qualified_path() )
    assert requestManager.get_fully_qualified_path() == "https://api.github.com/repos/teradici/deploy/commits?since=2022-02-07T00:00:00Z"

def test_invalid_date_parser_returns_None():
    requestManager = RequestManager("teradici", "deploy")
    date = requestManager.parse_date("fdsafasfasdfa")
    assert not date
