from enum import Enum

class ContentMessage(Enum):
    EXISTED = "existed"
    NOT_EXISTED = "not_existed"
    REQUIRED = "required"
    INVALID = 'invalid'
    INVALID_PASSWORD = 'invalid_password'
    INVALID_USERNAME = 'invalid_username'
    WRONG = 'wrong'