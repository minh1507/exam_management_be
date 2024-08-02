from rest_framework import viewsets, mixins
from App.models import Exam
from App.serializers import ExamSerializer

class ExamView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
    ):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer