from rest_framework.response import Response
from App.commons.enum import ReponseEnum
from App.commons.message import ResponseMessage

class ResponseDestroyOne:
    def __init__(self, data=None, status=ReponseEnum.SUCCESS.value, messages=[ResponseMessage.DESTROY_SUCCESS.value], toast=False):
        self.data = data
        self.status = status
        self.messages = messages
        self.toast = toast

    def to_response(self):
        response_data = {
            "status": self.status,
            "messages": self.messages,
            "data": self.data,
            "toast": self.toast
        }

        return Response(response_data)