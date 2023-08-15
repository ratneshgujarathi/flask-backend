from enum import Enum


class CollectionNames:
    # Core
    USERS = 'Users'
    EVENT_LOGS = 'EventLogs'
    TASKS_HISTORY = 'TaskHistory'
    SETTINGS = 'Settings'


class TaskStatuses:
    INPROGRESS = 'InProgress'
    SCHEDULED = 'Scheduled'
    COMPLETED = 'Completed'
    FAILED = 'Failed'
    QUEUED = 'Queued'
    ABORT = 'Abort'
    ABORTED = 'Aborted'
    SKIPPED = 'Skipped'
    WARNING = 'Warning'
    PARTIALLY_COMPLETED = 'Partially Completed'


class AppSettingNames:
    MIGRATIONS = 'Migrations'


class LogTypes:
    INFO = 'INFO'
    WARN = 'WARN'
    ERROR = 'ERROR'
    DEBUG = 'DEBUG'


class ModuleNames:
    pass


class ROLES:
    SUPER_ADMIN = 'Super Admin'
    USER = 'User'
    SYSTEM = 'system'


class SettingTypes:
    pass


class Permissions:
    VIEW_SETTINGS = 'VIEW_SETTINGS'
    VIEW_ACCOUNTS = 'VIEW_ACCOUNTS'
    ADD_ACCOUNTS = 'ADD_ACCOUNTS'
    UPDATE_ACCOUNTS = 'UPDATE_ACCOUNTS'
    DELETE_ACCOUNTS = 'DELETE_ACCOUNTS'
    VIEW_LOGS = 'VIEW_LOGS'
    EXPORT_LOGS = 'EXPORT_LOGS'
    VIEW_TASKS = 'VIEW_TASKS'
    ABORT_TASKS = 'ABORT_TASKS'
    VIEW_TASK = 'VIEW_TASK'
    ADD_ROLES = 'ADD_ROLES'
    DELETE_ROLES = 'DELETE_ROLES'
    VIEW_ROLES = 'VIEW_ROLES'
    EDIT_ROLES = 'EDIT_ROLES'
    VIEW_DASHBOARD = 'VIEW_DASHBOARD'
    EXPORT_DEBUG_LOG = 'EXPORT_DEBUG_LOG'


ACCESS_ROLES = {
    'SUPER_ADMIN': [
        Permissions.VIEW_SETTINGS, Permissions.VIEW_ACCOUNTS, Permissions.ADD_ACCOUNTS,
        Permissions.UPDATE_ACCOUNTS, Permissions.DELETE_ACCOUNTS,
        Permissions.VIEW_LOGS, Permissions.EXPORT_LOGS, Permissions.VIEW_TASKS,
        Permissions.ABORT_TASKS, Permissions.VIEW_TASK, Permissions.ADD_ROLES,
        Permissions.EDIT_ROLES, Permissions.VIEW_ROLES, Permissions.DELETE_ROLES,
        Permissions.VIEW_DASHBOARD, Permissions.EXPORT_DEBUG_LOG
    ],

    'USER': [
        Permissions.VIEW_ACCOUNTS, Permissions.VIEW_LOGS, Permissions.EXPORT_LOGS,
        Permissions.VIEW_TASKS, Permissions.VIEW_TASK, Permissions.VIEW_DASHBOARD
    ],

}


class Page:
    pass


class AccountStatus:
    VALID = 'valid'
    INVALID = 'invalid'
    EXISTING = 'exsting'


EXPONENTIAL_BACKOFF_REQUIRED_HTTP_STATUS_CODES = [403, 429, 500, 502, 503, 504]
DEFAULT_RETRY_INTERVAL = 30
EXPORT_COMMON_TIMESTAMP = '%Y%m%d_%H%M%S'
DEFAULT_LOG_RETENTION_PERIOD = 30
DEFAULT_TASK_RETENTION_PERIOD = 7


class ExportTrimSize(int, Enum):
    FOLDER_SIZE = 50
    FILE_SIZE = 50
