success = {
    "type": "object",
    "properties": {
        "result": {
            "type": "object"
        },
        "status": {
            "type": "string",
            "value": "success"
        }
    }
}

error = {
    "type": "object",
    "properties": {
        "error": {
            "type": "object",
            "properties": {
                "error_code": {
                    "type": "string",
                },
                "message": {
                    "type": "string",
                }
            }
        },
        "field": {
            "type": "string",
            "description": "[optional]"
        },
        "status": {
            "type": "string",
            "value": "error"
        }
    }
}
