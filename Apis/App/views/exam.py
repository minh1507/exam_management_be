from rest_framework import viewsets, mixins
from App.models import Exam
from App.models import Question
from App.serializers import ExamSerializer, ExamCreateSerializer, ExamDeleteSerializer, ExamValidate
import random
from datetime import datetime
from App.commons.response import (
    ResponseReadMany, ResponseReadOne, ResponseCreateOne, ResponseDestroyOne, ResponseBadRequest
)
from App.commons.message import ResponseMessage
from App.commons.enum import ReponseEnum
from App.commons.util import StringUtil

class ExamView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
    ):
    queryset = Exam.objects.all()
    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return ExamCreateSerializer
        return ExamSerializer
    
    def list(self, request, pk=None):
        exams = Exam.objects.filter(deletedAt__isnull=True).all()
        serializer = ExamSerializer(exams, many=True)

        return ResponseReadMany(
            data=serializer.data,
            total_count=len(serializer.data)
        ).to_response()
    
    def retrieve(self, request, pk):
        messages = ExamValidate.run(pk, 'pk')
        response = ResponseReadOne()
        if len(messages) == 0:
            exam = Exam.objects.get(pk=pk)
            serializer = ExamSerializer(exam)
            response.data=serializer.data,
        else:
            response.messages = messages
            response.status = ReponseEnum.BAD_REQUEST.value
            response.toast = True
        return response.to_response()
    
    def destroy(self, request, pk):
        messages = ExamValidate.run(pk, 'pk')
        response = ResponseDestroyOne()
        if len(messages) == 0:
            exam = Exam.objects.get(pk=pk)
            Exam.delete(exam)
            serializer = ExamDeleteSerializer(exam)
            response.data=serializer.data,
            response.toast = True
        else:
            response.messages = messages
            response.status = ReponseEnum.BAD_REQUEST.value
            response.toast = True
        return response.to_response()
    
    def create(self, request):
        messages = ExamSerializer.run(request.data, 'create')
        if len(messages) > 0:
            return ResponseBadRequest(messages=messages).to_response()
        response = ResponseCreateOne()

        serializer = ExamCreateSerializer(data=request.data)

        sumOfQuestion = serializer.validated_data.get('sumQuestion')
        if sumOfQuestion <= 0:
            return ResponseBadRequest(messages="Sum of question must be greater than 0").to_response()

        listAllQuestion = Question.objects.filter(subject = serializer.validated_data.get('subject'))
        listQuestion = []
        numOfQuestion = len(listAllQuestion)
        if sumOfQuestion < numOfQuestion:
            numbers = random.sample(range(0, numOfQuestion-1), sumOfQuestion)
            listQuestion = [listAllQuestion[i] for i in numbers]
        else:
            listQuestion = numOfQuestion

        exam_data={
            "code": serializer.validated_data.get('subject') + datetime.now(),
            "subject": serializer.validated_data.get('subject'),
            "supervisor": "",
            "expiredTime": serializer.validated_data.get('expiredTime'),
            "sumQuestion": serializer.validated_data.get('sumQuestion')
        }
        exam_serializer = ExamSerializer(data=exam_data)
        exam_serializer.is_valid(raise_exception=True)
        exam_serializer.save()

        if exam_serializer.is_valid() and len(messages)==0:
            newExam = exam_serializer.save()
            newExam.questions.set(listQuestion)
            response.data = serializer.data
            response.toast = True
        else:
            response.messages = messages
            response.status = ReponseEnum.BAD_REQUEST.value
            response.toast = True
            
        return response.to_response()  
