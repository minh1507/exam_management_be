from rest_framework.response import Response

class ResponseRead:
    def __init__(self, data, status="success", message="Find all successfully", total_count=None, toast=False):
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