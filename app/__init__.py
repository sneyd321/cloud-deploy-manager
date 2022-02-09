from flask import Flask, Response
from flask_caching import Cache

#init flask app
app = Flask(__name__)

#Define cache config
config = {
    "CACHE_TYPE": "RedisCache",  
    "CACHE_DEFAULT_TIMEOUT": 120,
    "CACHE_REDIS_HOST": "host.docker.internal",
    "CACHE_REDIS_PORT": 6379,
}

# tell Flask to use the above defined config
app.config.from_mapping(config)
#Initialize flask-caching
cache = Cache(app)

#General resource path to configure health checks
@app.route("/Health")
def health_check():
    return Response(status=200)


def create_app():
    #Create app
    global app
    #Intialize modules
    from app.api.routes import commit
    app.register_blueprint(commit, url_prefix="/")
    return app