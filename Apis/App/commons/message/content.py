from enum import Enum

class ContentMessage(Enum):
    EXISTED = "existed"
    REQUIRED = "required"
    INVALID = 'invalid'
    INVALID_PASSWORD = 'invalid_password'
    INVALID_USERNAME = 'invalid_username'