from rest_framework import viewsets, mixins
from App.models import User, Password, Profile
from App.serializers import (
    UserSerializer, UserValidate, UserDeleteSerializer, 
    PasswordSerializer, ProfileSerializer, RegisterValidate, UserCreateSerializer, UserChangeSerializer
)
from App.commons.response import (
    ResponseReadMany, ResponseReadOne, ResponseCreateOne, ResponseDestroyOne, ResponseBadRequest
)
from App.commons.message import ResponseMessage
from App.commons.enum import ReponseEnum
from App.commons.util import StringUtil

class SubjectView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
    ):
    queryset = Subject.objects.all()

    def list(self, request, pk=None):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)

        return ResponseReadMany(
            data=serializer.data,
            total_count=len(serializer.data)
        ).to_response()

    def create(self, request):
        messages = ProjectValidate.run(request.data)
        if len(message) > 0:
            return ResponseBadRequest(message=message).to_response()

        dataSerializer = ProjectCreateSerializer(data=request.data)
        dataSerializer.is_valid(raise_exception=True)
        dataSerializer.save()

        return ResponseCreateOne(
            messages=[ResponseMessage.CREATE_SUCCESS.value],
            status=ReponseEnum.CREATE.value,
            toast=True,
            data={"name": request.data.get("name")}
        ).to_response()

    
        