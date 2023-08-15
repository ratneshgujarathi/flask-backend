from swagger.components.parameters import header, body, query, path, form_data
from swagger.components.schemas.schemas import success, error
from swagger.components.responses.auth import AuthFailed
from swagger.components.responses.server_error import INTERNAL_ERROR
from swagger.components.securities.security import security
from swagger.defination.core_definations import (User)


def template(SERVER_IP='127.0.0.1', SERVER_PORT='9046', BASE_PATH='/'):
    return {
        "openapi": "2.0.0",
        "info": {
            "title": "Level 1 API",
            "description": "Level 1 Documentation",
            "version": "v1"
        },
        "schemes": [
            "http",
            "https"
        ],
        "operationId": "",
        "components": {
            "header": header.headers,
            "body": body.body,
            "query": query.query,
            "path": path.path,
            "formData": form_data.form_data,
            "securitySchemes": security,
            "responses": {
                "500": INTERNAL_ERROR
            },
            "schemas": {
                "success": success,
                "error": error
            },
        },
        "definitions": {
            "User": User,
            "AuthFailed": AuthFailed
        }

    }
