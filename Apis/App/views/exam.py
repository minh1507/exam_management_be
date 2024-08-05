from rest_framework import viewsets, mixins
from App.models import Exam
from App.models import Question, Subject, question
from App.serializers import ExamSerializer, ExamCreateSerializer, ExamDeleteSerializer, ExamValidate, ExamCreateManySerializer
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
        total = int(request.data['total_question'])
        question = Question.objects.filter(deletedAt__isnull=True, subject__id=request.data["subject"]).order_by('?')
        random_questions = question[:total]
        question_ids = [str(question.id) for question in random_questions]

        result = dict()
        result["questions"] = question_ids
        result['expired_time'] = request.data['expired_time']
        result['start_time'] = request.data['start_time']
        result['total_question'] = int(request.data['total_question'])
        result['supervisor'] = request.data['supervisor']
        result['code'] = request.data['code']
        result['subject'] = request.data['subject']

        serializer = ExamCreateManySerializer(data=result)

        data = None
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
        
        return ResponseCreateOne(data=data).to_response()  
