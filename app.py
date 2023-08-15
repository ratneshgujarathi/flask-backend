import json

from flasgger import Swagger
from flask import Flask, Response

from applications.core.api.v1 import core_v1
from applications.auth.api.v1 import auth
from config.config import load_config
from helpers.helper import JSONEncoder
from swagger.templates.template import template

app = Flask(__name__, instance_relative_config=True, static_url_path='/static')

# load app config
app.config.from_object(load_config(app.debug))

# JSON encoder
app.json_encoder = JSONEncoder

# Setup Swagger
swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'specifications',
            "route": '/specifications.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/level1/static",
    "specs_route": "/apidocs/"
}

# register api documentation
Swagger(
    app,
    template=template(
        app.config.get('SERVER_IP'),
        app.config.get('SERVER_PORT'),
        app.config.get('BASE_PATH')
    ),
    config=swagger_config
)


# Error handlers
@app.errorhandler(404)
def handle_not_found_error(error):
    return Response(
        response=json.dumps(
            {'error': {'error_code': 'not_found', 'message': str(error)}}),
        status=404,
        mimetype='application/json')


@app.errorhandler(405)
def handle_method_not_allowed_error(error):
    return Response(
        response=json.dumps(
            {'error': {'error_code': 'method_not_allowed', 'message': str(error)}}),
        status=405,
        mimetype='application/json')


@app.route('/')
def index():
    return 'ADVANCED API SERVER !!!'


app.config['SECRET_KEY'] = 'B0KS@PH2OI9'


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.after_request
def apply_caching(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE'
    return response


app.register_blueprint(core_v1)
app.register_blueprint(auth)

if __name__ == '__main__':
    app.run()
