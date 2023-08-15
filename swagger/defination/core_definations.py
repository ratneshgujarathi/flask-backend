User = {
    "type": "object",
    "properties": {
        "_id": {
            "type": "string",
            "description": "Boxafe user id",
            "required": True
        },
        "username": {
            "type": "string",
            "description": "Nas User name",
            "required": True
        },
        "is_admin": {
            "type": "boolean",
            "description": "Does is user boxafe admin",
        },
        "user_type": {
            "type": "string",
            "description": "User role in the boxafe ex. admin/user",
        },
        "name": {
            "type": "string",
            "description": "Name of the user in the NAS",
        },
        "created_at": {
            "type": "datetime",
            "description": "User created date and time",
        },
        "updated_at": {
            "type": "datetime",
            "description": "User updated date and time",
        },
        "created_by": {
            "type": "string",
            "description": "User ID who created current user",
        },
        "updated_by": {
            "type": "string",
            "description": "User ID who updated current user",
        },
        "is_active": {
            "type": "boolean",
            "description": "User active status in the Boxafe",
        }
    },
    "xml": {
        "name": "User"
    }
}
