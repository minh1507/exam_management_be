from rest_framework import viewsets
from App.models import Password, User, Profiling
from App.serializers import AuthSerializer,RegisterValidate,UserSerializer,PasswordSerializer,LoginValidate,ProfilingSerializer
from App.commons.response import ResponseCreateOne, ResponseBadRequest
from App.commons.enum import ReponseEnum
from rest_framework.decorators import action
from App.commons.util import StringUtil
from App.commons.message import ResponseMessage
from App.commons.message import KeyMessage, ContentMessage
from django.utils import timezone
from datetime import timedelta
import uuid
import jwt
import environ
env = environ.Env()
environ.Env.read_env()
class AuthView(
    viewsets.GenericViewSet
    ):
    queryset = User.objects.all()
    serializer_class = AuthSerializer

    @action(detail=False, methods=['post'], serializer_class=AuthSerializer)
    def login(self, request):
        messages = LoginValidate.run(request.data)

        if(len(messages) > 0):
            return ResponseBadRequest(messages).to_response() 
        
        dataSerializer = AuthSerializer(request.data)
        existUser = User.objects.select_related('password').select_related('role').filter(username=dataSerializer.data.get('username')).first()
        if(existUser is None):
            return ResponseBadRequest(messages=[StringUtil.messages(KeyMessage.USERNAME.value, ContentMessage.NOT_EXISTED.value)]).to_response() 
  
        if(StringUtil.compare_passwords(existUser.password.hash, dataSerializer.data.get('password')) == False):
            return ResponseBadRequest(messages=[StringUtil.messages(KeyMessage.PASSWORD.value, ContentMessage.WRONG.value)]).to_response() 
        
        payload = {
            "idp": str(uuid.uuid4()),
            "data": {
                "user": {
                    "username": existUser.username
                },
                "role": {
                    "code": existUser.role.code if existUser.role is not None else None
                }
            },
            "iat": timezone.now(),
            "exp": timezone.now() + timedelta(1)
        }

        data = dict()
        data["accessToken"] = jwt.encode(payload, env("ACCESS_TOKEN_KEY"), algorithm='HS256')

        payload['exp'] = timezone.now() + timedelta(365)
        data["refreshToken"] = jwt.encode(payload, env("REFRESH_TOKEN_KEY"), algorithm='HS256')

        return ResponseCreateOne(messages=[ResponseMessage.LOGIN_SUCCESS.value], data=data, toast=True, status=ReponseEnum.SUCCESS.value).to_response()

        