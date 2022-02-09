### cloud-deploy-manager
This is project for a technical interview for teradici. The goal was to develop a simple web application in Python, Go, or NodeJS that interacts with GitHub's REST API's and Teradici's public repository for Cloud Access
Manager.

This application is written in Python + Flask and deployed using Gunicorn.

#Running
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
