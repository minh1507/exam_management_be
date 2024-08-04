from rest_framework import viewsets, mixins
from App.models import Answer
from App.serializers import AnswerSerializer, AnswerCreateSerializer, AnswerValidate, AnswerDeleteSerializer
from App.commons.response import ResponseReadMany, ResponseReadOne, ResponseCreateOne, ResponseDestroyOne
from App.commons.enum import ReponseEnum
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
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

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'question_id', openapi.IN_QUERY, description="Question id", type=openapi.TYPE_STRING, required=True
            )
        ]
    )
    def list(self, request, pk=None):
        pk = request.query_params.get('question_id', None)
        answers = Answer.objects.select_related('question').filter(deletedAt__isnull=True, question__id=pk).all()
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
        messages = AnswerValidate.run(request.data, 'create', pk) + AnswerValidate.run(pk, 'pk')
        response = ResponseCreateOne()
        if(len(messages) > 0):
            response.messages = messages
            response.status = ReponseEnum.BAD_REQUEST.value
            response.toast = True
            return response.to_response() 
        
        answers = Answer.objects.get(pk=pk)
        serializer = AnswerCreateSerializer(instance=answers,data=request.data)
        if serializer.is_valid():
            serializer.save()
            response.data = serializer.data
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