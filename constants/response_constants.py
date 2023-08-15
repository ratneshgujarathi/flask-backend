RESPONSE_CONSTANTS = {
    # Application level keys, may applied generically
    'BAD_REQUEST': lambda status_code=400: ('Bad Request !!!', status_code),
    'REQUIRED_FIELD': lambda field, status_code=400: ("{0} field is required".format(', '.join(field)), status_code),
    'METHOD_NOT_ALLOWED': lambda status_code=405: ("The method is not allowed", status_code),
    'INTERNAL_SERVER_ERROR': lambda status_code=500: ('The server was unable to complete your request', status_code),
    'NON_ADMIN_USER': lambda status_code=403: ('User dont have required privileges. please contact administrator', status_code),
    'ACCESS_DENIED': lambda status_code=401: ('User dont have access to the resource. please contact administrator', status_code),

    # Resource CRUD errors, if specific error not defined then we can use from this
    'RESOURCE_ALREADY_EXISTS': lambda status_code=409: ('Resource already exists', status_code),
    'RESOURCE_NOT_FOUND': lambda status_code=409: ('The resource not found, it might be might be partially or completly deleted from system.', status_code),
    'RESOURCE_NOT_CREATED': lambda status_code=409: ('Failed to create', status_code),
    'RESOURCE_NOT_UPDATED': lambda status_code=409: ('Failed to update', status_code),
    'RESOURCE_NOT_DELETED': lambda status_code=409: ('Failed to delete', status_code),

    # Login
    'UNAUTHORIZED': lambda status_code=401: ('Authentication Failed.', status_code),
    'UNAUTHORIZED_FORBIDDEN': lambda status_code=403: ('Authentication Forbidden.', status_code),
    'INVALID_SECURITY_ANSWER': lambda status_code=401: ('Invalid Security Answer.', status_code),
    'INVALID_SECURITY_CODE': lambda status_code=401: ('Invalid Security Code.', status_code),

    # User Management
    'USER_NOT_FOUND': lambda status_code=409: ('User not found', status_code),
    'USER_ADD_FAILED': lambda status_code=409: ('User add failed', status_code),
    'USER_ALREADY_EXISTS': lambda status_code=409: ('User already exists', status_code),
    'USER_UPDATE_FAILED': lambda status_code=409: ('User update failed', status_code),
    'USER_DELETE_FAILED': lambda status_code=409: ('User delete failed', status_code),

    # Role Management
    'ROLE_ADD_FAILED': lambda status_code=409: ('Role add failed', status_code),
    'ROLE_ALREADY_EXISTS': lambda status_code=409: ('Role already exists', status_code),
    'ROLE_DELETE_FAILED': lambda status_code=409: ('Role delete failed', status_code),
    'INVALID_ROLE_NAME': lambda status_code=409: ('Role name is not valid', status_code),
    'ROLE_NOT_FOUND': lambda status_code=409: ('Role not found', status_code),
    'ROLE_DELETE_NOT_ALLOWED': lambda status_code=409: ('This role is assigned to other users. You can not delete this role', status_code),
    'ACCESS_PERMISSION_NOT_FOUND': lambda status_code=999: ("User don't have access to the resource. Please contact administrator", status_code),

    # Account
    'ACCOUNT_NOT_FOUND': lambda status_code=409: ('Account not found', status_code),
    'ACCOUNT_ADD_FAILED': lambda status_code=409: ('Account add failed', status_code),
    'ACCOUNT_UPDATE_FAILED': lambda status_code=409: ('Account update failed', status_code),
    'ACCOUNT_DELETE_FAILED': lambda status_code=409: ('Account delete failed', status_code),
    'ACCOUNTS_UPDATE_FAILED': lambda status_code=409: ('Accounts update failed', status_code),
    'ACCOUNTS_EXPORT_FAILED': lambda status_code=409: ('Accounts export failed', status_code),
    'INVALID_ACCOUNT_ID': lambda status_code=409: ('Given account id is invalid', status_code),
    'INVALID_FILE_FORMAT': lambda status_code=409: ('Given file format is invalid(CSV file only supported)', status_code),
    'INVALID_CSV_FILE': lambda status_code=409: ('Given CSV file is either empty or invalid', status_code),
    'HEADERS_NOT_FOUND': lambda status_code=409: ('No headers found in the file', status_code),

    # Logs
    'LOG_NOT_FOUND': lambda status_code=409: ('Log not found', status_code),
    'LOG_REMOVE_FAILED': lambda status_code=409: ('Failed to clear logs', status_code),
    'DOWNLOAD_LOG_FAILED': lambda status_code=409: ('Failed to download logs', status_code),
    'INVALID_LOG_RETENTIN_PERIOD': lambda status_code=409: ('Log retention period should greater than 29 and task retetion period should greater than 6', status_code),

    # Export
    'EXPORT_ERROR_FOLDER_NOT_EXISTS': lambda status_code=400: (f'The selected folder does not exist. Check if the folder has been removed.', status_code),
    'EXPORT_ERROR_FOLDER_PERMISSION_READ_ONLY': lambda status_code=400: (f'You only have read permission.', status_code),
    'EXPORT_ERROR_FOLDER_PERMISSION_DENIED': lambda status_code=400: (f'Folder access is denied.', status_code),
    'EXPORT_ERROR_FOLDER_PERMISSION_LOCKED': lambda status_code=400: (f'The shared folder is locked.', status_code),

    # Depricated
    'ALREADY_EXISTS': lambda field, status_code=409: ("{0} already exists".format(', '.join(field)), status_code),
    'DATABASE_RESOURCE_NOT_FOUND': lambda field, status_code=409: ("'{0}' field not found in database".format(*field), status_code),
    
    # License Center
    'LICENSE_REQUIRED': lambda status_code=400: ('License Required for this feature. Please purchase license from https://software.qnap.com/', status_code),
    'ACTIVATE_SEATS_NOT_SUFFICIENT': lambda status_code=400: ('Activation of given seats are exceeded the max limit or alloted license seats to your NAS', status_code),
    'LICENSE_INFORMATION_FETCH_FAILED': lambda status_code=400: ('Failed to fetch the license information. Please check the given id', status_code),
    'LICENSE_BLACKLISTED': lambda status_code=400: ('Your license has been blacklisted due to exceed the storage path limitation. Please contact support team.', status_code),
    'LICENSE_ASSIGN_USER_DUPLICATE_INSERTION': lambda status_code=400: ('The given user already have license. Duplicate insertion deducted', status_code),
    'LICENSE_ASSIGN_USER_FAILED': lambda status_code=400: ('Assigning user to the license failed', status_code),
    'LICENSE_ASSIGN_SHARED_DRIVE_FAILED': lambda status_code=400: ('Assigning shared drive to the license failed', status_code),
    'LICENSE_ASSIGN_SITES_FAILED': lambda status_code=400: ('Assigning sites to the license failed', status_code),
    'LICENSE_ASSIGN_TEAMS_FAILED': lambda status_code=400: ('Assigning teams to the license failed', status_code),
    'LICENSE_REASSIGN_USER_FAILED': lambda status_code=400: ('Reassigning user to the license failed', status_code),
    'LICENSE_REASSIGN_SITES_FAILED': lambda status_code=400: ('Reassigning sites to the license failed', status_code),
    'LICENSE_REASSIGN_TEAMS_FAILED': lambda status_code=400: ('Reassigning teams to the license failed', status_code),
    'LICENSE_REASSIGN_DRIVES_FAILED': lambda status_code=400: ('Reassigning shared drives to the license failed', status_code),
    'LICENSE_PRODUCT_TYPE_MISMATCH': lambda status_code=400: ('Please select the same product type license', status_code),
    'REASSIGN_UNSUPPORTED_SELECT_FREE_LICENSE':lambda status_code=400: ('Please select the free license. You can not assign paid license for Teams/Sites/Drives. System will automatically assign the paid license', status_code),
    'OLD_NEW_LICENSES_ARE_IDENTICAL': lambda status_code=400: ('Both old and new licenses are identical. Please select a new different license if you have purchased', status_code),
    'DEACTIVATE_SEATS_HAVE_DATA': lambda status_code=400: ('You are trying to deactivate the user license which have some data in Boxafe. Please delete the user data before proceed.', status_code),
    'LICENSE_UNASSIGN_USER_FAILED': lambda status_code=400: ('Unassigning user license failed', status_code),
    'LICENSE_UNASSIGN_SHARED_DRIVE_FAILED': lambda status_code=400: ('Unassigning shared drive license failed', status_code),
    'LICENSE_UNASSIGN_SITES_FAILED': lambda status_code=400: ('Unassigning sites license failed', status_code),
    'LICENSE_UNASSIGN_TEAMS_FAILED': lambda status_code=400: ('Unassigning teams license failed', status_code),
    'FETCHING_LICENSE_INFORMATION_FAILED': lambda status_code=400: ('Cannot get the license information for the given license id', status_code),
    'ACCOUNTS_ALREADY_LICENSED': lambda status_code=400: ('Given account already have license. Please deactivate it and assign the license', status_code),
    'SITES_ALREADY_LICENSED': lambda status_code=400: ('Given sites already have license. Please deactivate it and assign the license', status_code),
    'SHARED_DRIVE_ALREADY_LICENSED': lambda status_code=400: ('Given shared drives already have license. Please deactivate it and assign the license', status_code),
    'TEAMS_ALREADY_LICENSED': lambda status_code=400: ('Given teams already have license. Please deactivate it and assign the license', status_code),
    'NO_LICENSE_AVAILABLE': lambda status_code=400: ('No license available in Boxafe. Please contact our support team for best deals', status_code),
    'NO_LICENSE_SEATS_AVAILABLE': lambda status_code=400: ('No license seats are available in your existing Boxafe licenses or license seats are insufficient', status_code),
    'SHARE_DRIVE_ID_NOT_EXIST_IN_DB': lambda status_code=400: ('Some of the shared drive id is not exist in DB', status_code),
    'ACCOUNT_ID_NOT_EXIST_IN_DB': lambda status_code=400: ('Some of the account id is not exist in DB', status_code),
    'SITES_ID_NOT_EXIST_IN_DB': lambda status_code=400: ('Some of the sites id is not exist in DB', status_code),
    'TEAMS_ID_NOT_EXIST_IN_DB': lambda status_code=400: ('Some of the teams id is not exist in DB', status_code),
    'LICENSE_EXPIRED': lambda status_code=400: ('License for this request has been expired. Please purchase or renew the license', status_code),
    'LICENSE_POST_METHOD_REQUIRED': lambda status_code=400: ('Only post method & json payload allowed for this request', status_code),
    'LICENSE_SYNC_NOT_UPDATED': lambda status_code=400: ('Cloud licenses not updated for longer period of time. Please check your network', status_code),
    # 'ACCESS_DENIED': lambda status_code=400: ('Access denied for the given request.', status_code),
    'INVALID_LICENSE_ID': lambda status_code=409: ('Given license id is invalid', status_code),

    # Settings
    'INVALID_CONCURRENCY_CONFIGURATION': lambda status_code=409: ('Given concurrency number is invalid', status_code),
    'INVALID_MEMORY_ALLOCATION_CONFIGURATION': lambda status_code=409: ('Given memory allocation is invalid', status_code)

}

