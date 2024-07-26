from rest_framework import viewsets
from App.models import Password, User
from App.serializers import AuthSerializer,RegisterValidate,UserSerializer,PasswordSerializer,LoginValidate
from App.commons.response import ResponseCreateOne, ResponseBadRequest
from App.commons.enum import ReponseEnum
from rest_framework.decorators import action
from App.commons.util import StringUtil
from App.commons.message import ResponseMessage
from App.commons.message import KeyMessage, ContentMessage
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

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
        existUser = User.objects.select_related('password').filter(username=dataSerializer.data.get('username')).first()
        
        if(existUser is None):
            return ResponseBadRequest(messages=[ContentMessage.NOT_EXISTED.value + '.' + KeyMessage.USERNAME.value]).to_response() 
  
        if(StringUtil.compare_passwords(existUser.password.hash, dataSerializer.data.get('password')) == False):
            return ResponseBadRequest(messages=[ContentMessage.WRONG.value + '.' + KeyMessage.PASSWORD.value]).to_response() 
        
        refresh = AccessToken.for_user(existUser)
        print(refresh)

        return ResponseCreateOne(messages=[ResponseMessage.LOGIN_SUCCESS.value], toast=True, status=ReponseEnum.SUCCESS.value).to_response()
    
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

        userSerializer = UserSerializer(data=account)
     
        if userSerializer.is_valid():
            userSerializer.save()
        return ResponseCreateOne(messages=[ResponseMessage.REGISTER_SUCCESS.value], status=ReponseEnum.CREATE.value, toast=True, data={"username": request.data.get("username")}).to_response()
   
        