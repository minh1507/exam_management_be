from enum import Enum

class ContentMessage(Enum):
    EXISTED = "existed"
    REQUIRED = "required"
    INVALID = 'invalid'