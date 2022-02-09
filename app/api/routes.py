from . import commit
from flask import jsonify, request, Response, abort
from app.api.repository import CommitRepository
from app.api.request import RequestManager
from app import cache

commitRepository = CommitRepository()
requestManager = RequestManager("teradici", "deploy")
#requestManager.add_authorization("")
requestManager.add_query_param("page", 1)
requestManager.add_query_param("per_page", 100)
PAGE_LIMIT = 5



def is_query_params_valid(start, end):
    #If parameters exists
    if not start or not end:
        return False
    since = requestManager.parse_date(start)
    until = requestManager.parse_date(end)
    #If start and end are in valid format
    if not since or not until:
        return False
    #If start is after end
    if since > until:
        return False
    #Set date query parameters
    requestManager.add_date_query_param("since", since)
    requestManager.add_date_query_param("until", until)
    return True



@commit.route("/users")
@cache.cached(timeout=120, query_string=True)
def users():
    #Get query params
    start = request.args.get('start')
    end = request.args.get('end')

    #If query params are not valid
    if not is_query_params_valid(start, end):
        return Response(status=400)
    
    #Call Github Commit API
    response = requestManager.get(PAGE_LIMIT)
   
    users = commitRepository.get_users(response, start, end)
    return jsonify(users)
        
@commit.route("/most-frequent")
@cache.cached(timeout=120, query_string=True)
def most_frequent():
    #Get query params
    start = request.args.get('start')
    end = request.args.get('end')

    #If query params are not valid
    if not is_query_params_valid(start, end):
        return Response(status=400)
    
    #Call Github Commit API
    response = requestManager.get(PAGE_LIMIT)

    authors = commitRepository.get_authors(response, start, end)
    frequentCommitters = commitRepository.get_frequent_committers_as_list(authors)

    #If number of committers are less than 5 return the list, otherwise return top 5
    if (len(frequentCommitters) < 5):
        return jsonify(frequentCommitters)
    return jsonify(frequentCommitters[:5])