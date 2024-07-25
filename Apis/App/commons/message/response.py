from enum import Enum

class ResponseMessage(Enum):
    FIND_SUCCESS = "success.find"
    CREATE_SUCCESS = "success.create"
    DESTROY_SUCCESS = "success.destroy"