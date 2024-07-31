from enum import Enum

class ResponseMessage(Enum):
    FIND_SUCCESS = "success.find"
    CREATE_SUCCESS = "success.create"
    UPDATE_SUCCESS = "success.update"
    DESTROY_SUCCESS = "success.destroy"
    REGISTER_SUCCESS = "success.register"
    LOGIN_SUCCESS = "success.login",
    UNAUTHORIZE = "failed.unauthorize"