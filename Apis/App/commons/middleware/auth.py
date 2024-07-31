from django.http import JsonResponse
class AuthorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Authorization logic
        if not self.is_authorized(request):
            return JsonResponse({
            "status": 401,
            "messages": "failed.unauthorize",
            "data": None,
            "toast": True
        }, status=401)
        
        response = self.get_response(request)
        return response

    def is_authorized(self, request):
        excluded_paths = ['api/auth/login']
        if request.path in excluded_paths:
            return True
        else:
            auth_header = request.headers.get('Authorization')
            if(auth_header):
                return True;
            else: 
                return False
