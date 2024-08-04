from django.http import JsonResponse
import jwt
import environ
env = environ.Env()
environ.Env.read_env()
from django.core.cache import cache

class AuthorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not self.is_authorized(request):
            return JsonResponse({
            "status": 401,
            "messages": ["failed.unauthorize"],
            "data": None,
            "toast": True
        }, status=401)
        
        response = self.get_response(request)
        return response

    def is_authorized(self, request):
        excluded_paths = ['/api/auth/login/', '/api/auth/login', '/apis/', '/apis']
        try:
            if request.path in excluded_paths:
                return True
            else:
                auth_header = request.headers.get('Authorization')
                if(auth_header):
                    result = jwt.decode(auth_header, env("ACCESS_TOKEN_KEY"), algorithms='HS256')
                    access_token = cache.get(result["data"]["access_key"])
                    if access_token is not None:
                        return True
                    return False
                else: 
                    return False
        except:
            return False        
            
            
