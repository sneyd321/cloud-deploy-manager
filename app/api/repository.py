from app.api.models import Commit

class CommitRepository:
    """Repository class for Commits"""

    def get_users(self, response, start, end):
        """Get all users from the Githib Commits API
        start: date in format YYYY-MM-DD
        end: date in format YYYY-MM-DD
        Returns: list of dicts containing the email and name of the commit author
        """
        users = []
        for item in response:
            user = Commit(**item["commit"]).get_user(start, end)
            if user:
                users.append(user)
        return users

    def get_authors(self, response, start, end):
        """Get all authors from the Githib Commits API
        start: date in format YYYY-MM-DD
        end: date in format YYYY-MM-DD
        Returns: list of Author objects
        """
        authors = []
        for item in response:
            author = Commit(**item["commit"]).get_author(start, end)
            if author:
                authors.append(author)
        return authors
        
    def get_frequent_committer(self, authors, email):
        """Counts how the number of authors assoicated with an email 
        authors: list of Authors 
        email: str
        Returns: dict with the number of commits and name of author
        """
        frequentCommitter = {
            "commits": 0,
            "name": ""
        }
        for author in authors:
            if author.get_email() != email:
                continue
            frequentCommitter["commits"] += 1
            frequentCommitter["name"] = author.get_name()
        return frequentCommitter

    def get_frequent_committers_as_list(self, authors):
        """Gets list of all frequent committers
        authors: list of Authors 
        Returns: sorted list decending of all frequent committers
        """
        emails = [author.get_email() for author in authors]
        uniqueEmails = list(set(emails))
        frequentCommitters = [self.get_frequent_committer(authors, email) for email in uniqueEmails]
        return sorted(frequentCommitters, key=lambda d: d['commits'], reverse=True) 
       

        

            
     


        