from rest_framework.response import Response
from App.commons.enum import ReponseEnum
from App.commons.message import ResponseMessage

class ResponseBadRequest:
    def __init__(self, messages=[ResponseMessage.CREATE_SUCCESS.value]):
        self.data = None
        self.status = ReponseEnum.BAD_REQUEST.value
        self.messages = messages
        self.toast = True

    def to_response(self):
        response_data = {
            "status": self.status,
            "messages": self.messages,
            "data": self.data,
            "toast": self.toast
        }

        return Response(response_data, status=self.status)