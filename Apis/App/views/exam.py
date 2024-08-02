from rest_framework import viewsets, mixins
from App.models import Exam
from App.serializers import QuestionDeleteSerializer, QuestionSerializer, QuestionValidate, ExamSerializer
from App.commons.response import ResponseReadMany, ResponseReadOne, ResponseCreateOne, ResponseDestroyOne
from App.commons.enum import ReponseEnum

class ExamView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
    ):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer