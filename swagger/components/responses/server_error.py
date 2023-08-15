from swagger.components.schemas.schemas import error

INTERNAL_ERROR = {
    "description": "INTERNAL SERVER ERROR",
    "schema": error,
    "examples": {
        "": {
            "error": {
                "error_code": "INTERNAL_SERVER_ERROR",
                "message": "The server was unable to complete your request"
            },
            "status": "error"
        }
    }
}
