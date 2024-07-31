from rest_framework import viewsets, mixins
from App.models import User
from App.serializers import (
    UserSerializer, UserValidate, UserDeleteSerializer, 
    PasswordSerializer, RegisterValidate, UserCreateSerializer, UserChangeSerializer, ProfilingSerializer
)
from App.commons.response import (
    ResponseReadMany, ResponseReadOne, ResponseCreateOne, ResponseDestroyOne, ResponseBadRequest
)
from App.commons.message import ResponseMessage
from App.commons.enum import ReponseEnum
from App.commons.util import StringUtil

class UserView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return UserCreateSerializer
        return UserSerializer

    def list(self, request, pk=None):
        users = User.objects.select_related('role', 'profiling').exclude(role__code="ADMIN").filter(deletedAt__isnull=True).all()
        serializer = UserSerializer(users, many=True)
        return ResponseReadMany(
            data=serializer.data,
            total_count=len(serializer.data)
        ).to_response()

    def retrieve(self, request, pk):
        messages = UserValidate.run(pk, 'pk')
        response = ResponseReadOne()
        if len(messages) == 0:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            response.data = serializer.data
        else:
            response.messages = messages
            response.status = ReponseEnum.BAD_REQUEST.value
            response.toast = True
        return response.to_response()

    def create(self, request, *args, **kwargs):
        messages = RegisterValidate.run(request.data)
        if len(messages) > 0:
            return ResponseBadRequest(messages=messages).to_response()

        dataSerializer = UserCreateSerializer(data=request.data)
        dataSerializer.is_valid(raise_exception=True)

        password_data = {
            "hash": StringUtil.hash_password_with_key(dataSerializer.validated_data.get("password"))
        }
        passwordSerializer = PasswordSerializer(data=password_data)
        passwordSerializer.is_valid(raise_exception=True)
        resultPassword = passwordSerializer.save()

        profile_data = {"lastname": "New user"}
        profileSerializer = ProfilingSerializer(data=profile_data)
        profileSerializer.is_valid(raise_exception=True)
        profiling = profileSerializer.save()

        account_data = {
            "username": dataSerializer.validated_data.get("username"),
            "password": str(resultPassword),
            "role": dataSerializer.validated_data.get("role"),
            "profiling": profiling.id
        }
        
        userSerializer = UserChangeSerializer(data=account_data)
        userSerializer.is_valid(raise_exception=True)
        userSerializer.save()

        return ResponseCreateOne(
            messages=[ResponseMessage.CREATE_SUCCESS.value],
            status=ReponseEnum.CREATE.value,
            toast=True,
            data={"username": request.data.get("username")}
        ).to_response()

    def destroy(self, request, pk):
        messages = UserValidate.run(pk, 'pk')
        response = ResponseDestroyOne()
        if len(messages) == 0:
            user = User.objects.get(pk=pk)
            user.delete()
            serializer = UserDeleteSerializer(user)
            response.data = serializer.data
            response.toast = True
        else:
            response.messages = messages
            response.status = ReponseEnum.BAD_REQUEST.value
            response.toast = True
        return response.to_response()
