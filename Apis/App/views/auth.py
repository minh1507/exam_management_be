from rest_framework import viewsets
from App.models import Ethnic, Password
from App.serializers import EthnicSerializer,AuthSerializer,RegisterValidate,UserSerializer,PasswordSerializer
from App.commons.response import ResponseCreateOne
from App.commons.enum import ReponseEnum
from rest_framework.decorators import action
from App.commons.util import StringUtil
from App.commons.message import ResponseMessage
import json
class AuthView(
    viewsets.GenericViewSet
    ):
    queryset = Ethnic.objects.all()
    serializer_class = AuthSerializer

    @action(detail=False, methods=['post'], serializer_class= AuthSerializer)
    def login(self, request):
        serializer = AuthSerializer(request.data)
        response = ResponseCreateOne()
        response.data = serializer.data
        return response.to_response()
    
    @action(detail=False, methods=['post'], serializer_class=AuthSerializer)
    def register(self, request):
        messages = RegisterValidate.run(request.data, 'create')

        response = ResponseCreateOne()
        if(len(messages) > 0):
            response.messages = messages
            response.status = ReponseEnum.BAD_REQUEST.value
            response.toast = True
            return response.to_response() 
        
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

        userSerializer = UserSerializer(data=account)
     
        if userSerializer.is_valid():
            userSerializer.save()

        response.messages = [ResponseMessage.REGISTER_SUCCESS.value]
        response.status = ReponseEnum.SUCCESS.value
        response.toast = True
        response.data = {"username": request.data.get("username")}
        return response.to_response()
   
        