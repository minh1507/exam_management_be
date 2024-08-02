from rest_framework import viewsets, mixins
from App.models import Answer, Question
from App.serializers import AnswerSerializer, AnswerCreateSerializer, AnswerValidate, AnswerDeleteSerializer
from App.commons.response import ResponseReadMany, ResponseReadOne, ResponseCreateOne, ResponseDestroyOne
from App.commons.enum import ReponseEnum

class AnswerView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
    ):
    queryset = Answer.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return AnswerCreateSerializer
        return AnswerSerializer

    
    def list(self, request, pk=None):
        answers = Answer.objects.filter(deletedAt__isnull=True).all()
        serializer = AnswerSerializer(answers, many=True)

        return ResponseReadMany(
            data=serializer.data,
            total_count=len(serializer.data)
        ).to_response()
    
    def retrieve(self, request, pk):
        messages = AnswerValidate.run(pk, 'pk')
        response = ResponseReadOne()
        if len(messages) == 0:
            answer = Answer.objects.get(pk=pk)
            serializer = AnswerSerializer(answer)
            response.data=serializer.data,
        else:
            response.messages = messages
            response.status = ReponseEnum.BAD_REQUEST.value
            response.toast = True
        return response.to_response()
    
    def create(self, request):
        messages = AnswerValidate.run(request.data, 'create')
        response = ResponseCreateOne()

        serializer = AnswerCreateSerializer(data=request.data)
        answer_data = {
            "questionId": Question.objects.get(id=serializer.validated_data.get("questionId")),
            "content": serializer.validated_data.get("content"),
            "isResult": serializer.validated_data.get("isResult")
        }
        answerSerializer = AnswerSerializer(data = answer_data)
        answerSerializer.is_valid(raise_exception=True)
        answerSerializer.save()

        if serializer.is_valid() and len(messages)==0:
            serializer.save()
            response.data = serializer.data
            response.toast = True
        else:
            response.messages = messages
            response.status = ReponseEnum.BAD_REQUEST.value
            response.toast = True
            
        return response.to_response()  
    
    def update(self, request, pk):
        messages = AnswerValidate.run(request.data, 'update', pk) + AnswerValidate.run(pk, 'pk')
        response = ResponseCreateOne()
        if(len(messages) > 0):
            response.messages = messages
            response.status = ReponseEnum.BAD_REQUEST.value
            response.toast = True
            return response.to_response() 
        
        answers = Answer.objects.get(pk=pk)
        serializer = AnswerCreateSerializer(data=request.data, instance=answers)
        answer_data = {
            "questionId": Question.objects.get(id=serializer.validated_data.get("questionId")),
            "content": serializer.validated_data.get("content"),
            "isResult": serializer.validated_data.get("isResult")
        }
        answerSerializer = AnswerSerializer(data = answer_data)

        if answerSerializer.is_valid():
            answerSerializer.save()
            response.data = answerSerializer.data
            response.toast = True
            response.status = ReponseEnum.SUCCESS.value
        return response.to_response() 
    
    def destroy(self, request, pk):
        messages = AnswerValidate.run(pk, 'pk')
        response = ResponseDestroyOne()
        if len(messages) == 0:
            answer = Answer.objects.get(pk=pk)
            Answer.delete(answer)
            serializer = AnswerDeleteSerializer(answer)
            response.data=serializer.data,
            response.toast = True
        else:
            response.messages = messages
            response.status = ReponseEnum.BAD_REQUEST.value
            response.toast = True
        return response.to_response()