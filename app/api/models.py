from datetime import datetime

class Date:

    def __init__(self, date):
        self._date = datetime.strptime(date,'%Y-%m-%dT%H:%M:%SZ')

    def get_date(self):
        return self._date

class User:
    def __init__(self, **kwargs):
        self._date = Date(kwargs.get("date"))
        self._email = kwargs.get("email")
        self._name = kwargs.get("name")

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def get_date(self):
        return self._date.get_date()

class Author(User):
    def __init__(self, **kwargs):
        User.__init__(self, **kwargs)

class Commiter(User):
    def __init__(self, **kwargs):
        User.__init__(self, **kwargs)

class Tree:
    def __init__(self, **kwargs):
        self._sha = kwargs.get("sha")
        self._url = kwargs.get("url")

class Commit:
    def __init__(self, **kwargs):
        self._author = Author(**kwargs.get("author"))
        self._comment_count = kwargs.get("comment_count")
        self._committer = Commiter(**kwargs.get("committer"))
        self._message = kwargs.get("message")
        self._tree = Tree(**kwargs.get("tree"))
        self._url = kwargs.get("url")
        self._verification = kwargs.get("verification")
        self._payload = kwargs.get("payload")
        self._reason = kwargs.get("reason")
        self._signature = kwargs.get("signature")
        self._verified = kwargs.get("verified")

    def get_email(self):
        return self._author.get_email()

    def get_name(self):
        return self._author.get_name()
      
    def get_date(self):
        return self._author.get_date()



    def is_date_valid(self, start, end):
        """Checks if starting date and the ending date are valid
        start: str
        end: str
        Returns: bool 
        """
        try:
            startTime = datetime.strptime(start,'%Y-%m-%d')
            endTime = datetime.strptime(end,'%Y-%m-%d')
        except (ValueError, TypeError):
            return False
        return self.get_date() > startTime and self.get_date() < endTime

  
    def get_user(self, start, end):
        """Returns the name and email as a dict between a valid date range
        start: date in format YYYY-MM-DD
        end: date in format YYYY-MM-DD
        Returns: dict with the name and email of the Commit Author
        """
        if not self.is_date_valid(start, end):
           return None 
        return {
            "name": self.get_name(),
            "email": self.get_email()
        }


    def get_author(self, start, end):
        """Returns the Author between a valid date range
        start: date in format YYYY-MM-DD
        end: date in format YYYY-MM-DD
        Returns: Author
        """
        if not self.is_date_valid(start, end):
            return None 
        return self._author

