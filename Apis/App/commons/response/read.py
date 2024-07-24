from rest_framework.response import Response
from ..enum.reponse import ReponseEnum
from ..message.response import ResponseMessage
class ResponseRead:
    def __init__(self, data, status:int=ReponseEnum.SUCCESS.value, message:list=[ResponseMessage.FIND_ALL_SUCCESS].value, total_count=None, toast=False):
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