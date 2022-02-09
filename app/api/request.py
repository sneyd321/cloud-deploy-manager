import requests, os
from datetime import datetime

class RequestManager:
  
    def __init__(self, owner, repo):
        self._owner = owner
        self._repo = repo
        self._endpoint = "https://api.github.com"
        self._resource = f"/repos/{self._owner}/{self._repo}/commits"
        self._headers= {"accept": "application/vnd.github.v3+json"}
        self._query_params = {}

    def add_authorization(self, token):
        self._headers["Authorization"] = f"token {token}"

    def add_query_param(self, name, value):
        self._query_params[name] = value

    def parse_date(self, date):
        try: 
            date = datetime.strptime(date,'%Y-%m-%d')
        except (TypeError, ValueError):
            return None
        return date

    
    def add_date_query_param(self, name, date):
        value = datetime.strftime(date,'%Y-%m-%dT%H:%M:%SZ')
        self._query_params[name] = value

    def get_fully_qualified_path(self):
        url = self._endpoint + self._resource
        isFirst = True
        for name, value in self._query_params.items():
            if isFirst:
                url += f"?{name}={value}"
                isFirst = False
                continue
            url += f"&{name}={value}"
        return url



    def get(self, page_limit):
        commits = []
        page = 1
        while page <= page_limit:
            response = requests.get(self.get_fully_qualified_path(), headers=self._headers)
            if not response.ok:
                continue
            responseAsJson = response.json()
            #If response is empty list
            if not responseAsJson:
                break
            commits.extend(responseAsJson)
            page += 1
        return commits