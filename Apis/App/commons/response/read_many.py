from rest_framework.response import Response
from App.commons.enum import ReponseEnum
from App.commons.message import ResponseMessage

class ResponseReadMany:
    def __init__(self, data, status=ReponseEnum.SUCCESS.value, message=[ResponseMessage.FIND_ALL_SUCCESS.value], total_count=None, toast=False):
        self.data = data
        self.status = status
        self.message = message
        self.total_count = total_count
        self.toast = toast

    def to_response(self):
        response_data = {
            "status": self.status,
            "message": self.message,
            "data": self.data,
            "toast": self.toast
        }
        if self.total_count is not None:
            response_data["total_count"] = self.total_count
        return Response(response_data)