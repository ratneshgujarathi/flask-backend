AuthFailed = {
    "type": "object",
    "properties": {
        "status": {
            "type": "string",
            "description": "status of the request",
            "default": "error"
        },
        "error": {
            "type": "object",
            "description": "Error object",
            "properties": {
                "error_code": {
                    "type": "string"
                },
                "message": {
                    "type": "string"
                },
                "fields": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                }
            },
        }
    },
    "xml": {
        "name": "AuthFailed"
    }
}
