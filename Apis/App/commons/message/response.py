from enum import Enum

class ResponseMessage(Enum):
    # find all
    FIND_ALL_SUCCESS = "Find all successfully"
    FIND_ALL_FAILED = "Find all failed"

    # find one
    FIND_ONE_SUCCESS = "Find one successfully"
    FIND_ONE_FAILED = "Find one failed"