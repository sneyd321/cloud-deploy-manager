### Cloud Access Manager
This is project for a technical interview for Teradici. The goal was to develop a simple web application in Python, Go, or NodeJS that interacts with GitHub's REST API's and Teradici's public repository for Cloud Access.

This application is written in Python + Flask and deployed using Gunicorn.

## Running
After cloning the repoistory run
```
docker-compose build
```
Then,
```
docker-compose up
```
If getting empty lists returned or test case failures, please add a personal access token to the TOKEN environment variable in the docker-compose file
```yaml
cloud-deploy-manager-service:
        build: .
        ports: 
            - 8080:8080
        restart: on-failure
        environment:
         - PORT=8080
         - TOKEN=""
        volumes: 
            - ./:/usr/src/app
```
## Testing
To test the code run
```
docker-compose run cloud-deploy-manager-service pytest  
```
## Design Choices
The server deployed as a repository style architecture. I chose this because I think i provides a nice layer of abstraction between the models I defined and the application logic handleing the request.

Instead of parsing the response data directly I decided to use keyword arguments to map the response into python objects. This was done to increase the readablility and maintainability of the server. Using python objects also allows for more extendability for the server if it was required to do anything further.

For managing the cache I used the flask_caching. This was done to minimize the effort of managing redis queries and not requiring a whole seperate class to manage redis configuration. This also allowed my view functions to be decorated with the cached decorator making it easier to add more caching options if required.

The server is configured using flask blueprints. This allows for api versioning if required and decouples the api from any other future work that may be required.

For implementing the bonus I removed the default behaviour of only using the date range between June 1, 2019 - May 31, 2020 to any date range entered by the user. I thought it would be confusing behaviour to someone consuming the API to not include query parameters and have a random (from their perspective) date range used.

For mocking I used postman.

For testing all my automated tests test were broken into two types date validation and verifying the existence of entities. 
The date validation is based on the requiement June 1, 2019 - May 31, 2020
The null check tests were done to verify the api is not returning an empty list. The verification of data output was done manually.








