from rest_framework import viewsets, mixins
from App.models import Question, Subject
from App.serializers import QuestionDeleteSerializer, QuestionSerializer, QuestionValidate, QuestionCreateSerializer
from App.commons.response import ResponseReadMany, ResponseReadOne, ResponseCreateOne, ResponseDestroyOne
from App.commons.enum import ReponseEnum

class QuestionView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
    ):
    queryset = Question.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return QuestionCreateSerializer
        return QuestionSerializer

    def list(self, request, pk=None):
        questions = Question.objects.filter(deletedAt__isnull=True).all()
        serializer = QuestionSerializer(questions, many=True)

        return ResponseReadMany(
            data=serializer.data,
            total_count=len(serializer.data)
        ).to_response()
    
    def retrieve(self, request, pk):
        messages = QuestionValidate.run(pk, 'pk')
        response = ResponseReadOne()
        if len(messages) == 0:
            question = Question.objects.get(pk=pk)
            serializer = QuestionSerializer(question)
            response.data=serializer.data,
        else:
            response.messages = messages
            response.status = ReponseEnum.BAD_REQUEST.value
            response.toast = True
        return response.to_response()
    
    def create(self, request):
        messages = QuestionValidate.run(request.data, 'create')
        response = ResponseCreateOne()

        serializer = QuestionCreateSerializer(data=request.data)
        question_data = {
            "code": serializer.validated_data.get("code"),
            "subject": Subject.objects.get(code=serializer.validated_data.get("subjectCode")),
            "lecturer": serializer.validated_data.get("lecturer"),
            "question": serializer.validated_data.get("question"),
            "mark": serializer.validated_data.get("mark"),
            "unit": serializer.validated_data.get("unit"),
            "mixChoices": serializer.validated_data.get("mixChoices"),
            "imageId" : serializer.validated_data.get("imageId")
        }
        questionSerializer = QuestionSerializer(data = question_data)
        questionSerializer.is_valid(raise_exception=True)
        questionSerializer.save()

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
        messages = QuestionValidate.run(request.data, 'update', pk) + QuestionValidate.run(pk, 'pk')
        response = ResponseCreateOne()
        if(len(messages) > 0):
            response.messages = messages
            response.status = ReponseEnum.BAD_REQUEST.value
            response.toast = True
            return response.to_response() 
        
        questions = Question.objects.get(pk=pk)
        # serializer = QuestionSerializer(instance=questions,data=request.data)
        serializer = QuestionCreateSerializer(data=request.data, instance=questions)
        question_data = {
            "code": serializer.validated_data.get("code"),
            "subject": Subject.objects.get(code=serializer.validated_data.get("subjectCode")),
            "lecturer": serializer.validated_data.get("lecturer"),
            "question": serializer.validated_data.get("question"),
            "mark": serializer.validated_data.get("mark"),
            "unit": serializer.validated_data.get("unit"),
            "mixChoices": serializer.validated_data.get("mixChoices"),
            "imageId" : serializer.validated_data.get("imageId")
        }
        questionSerializer = QuestionSerializer(data = question_data)

        if questionSerializer.is_valid():
            questionSerializer.save()
            response.data = questionSerializer.data
            response.toast = True
            response.status = ReponseEnum.SUCCESS.value
        return response.to_response() 
    
    def destroy(self, request, pk):
        messages = QuestionValidate.run(pk, 'pk')
        response = ResponseDestroyOne()
        if len(messages) == 0:
            question = Question.objects.get(pk=pk)
            Question.delete(question)
            serializer = QuestionDeleteSerializer(question)
            response.data=serializer.data,
            response.toast = True
        else:
            response.messages = messages
            response.status = ReponseEnum.BAD_REQUEST.value
            response.toast = True
        return response.to_response()
        