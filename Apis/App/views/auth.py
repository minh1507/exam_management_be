from rest_framework import viewsets
from App.models import Password, User, Profile
from App.serializers import AuthSerializer,RegisterValidate,UserSerializer,PasswordSerializer,LoginValidate,ProfileSerializer
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
        print(existUser.role.name)
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
                    "code": existUser.role.code
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
    
    @action(detail=False, methods=['post'], serializer_class=AuthSerializer)
    def register(self, request):
        messages = RegisterValidate.run(request.data)

        if(len(messages) > 0):
            return ResponseBadRequest(messages=messages).to_response() 
        
        dataSerializer = AuthSerializer(request.data)

        password = dict()
        password["hash"] = StringUtil.hash_password_with_key(dataSerializer.to_data().get("password"))

        resultPassword = Password()
        passwordSerializer = PasswordSerializer(data=password)
        if passwordSerializer.is_valid():
            resultPassword = passwordSerializer.save()

        account = dict()
        account["username"] = dataSerializer.to_data().get("username")
        account["password"] = str(resultPassword)
        account['role'] = "00000000000000000000000000000001"

        userSerializer = UserSerializer(data=account)
     
        if userSerializer.is_valid():
            userSerializer.save()

        profileSerializer = ProfileSerializer(data={"firstname": "New user"})

        if profileSerializer.is_valid():
            profileSerializer.save()
            
        return ResponseCreateOne(messages=[ResponseMessage.REGISTER_SUCCESS.value], status=ReponseEnum.CREATE.value, toast=True, data={"username": request.data.get("username")}).to_response()
   
        