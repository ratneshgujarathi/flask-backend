security = {
    "BasicAuth": {
        "type": "http",
        "scheme": "basic"
    },
    "BearerAuth": {
        "type": "http",
        "scheme": "bearer"
    },
    "ApiKeyAuth": {
        "type": "apiKey",
        "in": "header",
        "name": "X-API-Key"
    }
}
