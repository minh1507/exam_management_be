from rest_framework.response import Response
from App.commons.enum import ReponseEnum
from App.commons.message import ResponseMessage

class ResponseReadOne:
    def __init__(self, data, status=ReponseEnum.SUCCESS.value, message=[ResponseMessage.FIND_ONE_SUCCESS.value], toast=False):
        self.data = data
        self.status = status
        self.message = message
        self.toast = toast

    def to_response(self):
        response_data = {
            "status": self.status,
            "message": self.message,
            "data": self.data,
            "toast": self.toast
        }

        return Response(response_data)