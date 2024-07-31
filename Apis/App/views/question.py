from rest_framework import viewsets, mixins
from App.models import Question
from App.serializers import QuestionDeleteSerializer, QuestionSerializer, QuestionValidate
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
    serializer_class = QuestionSerializer

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
            "ansA": serializer.validated_data.get("ansA"),
            "ansB": serializer.validated_data.get("ansB"),
            "ansC": serializer.validated_data.get("ansC"),
            "ansD": serializer.validated_data.get("ansD"),
            "answer": serializer.validated_data.get("answer"),
            "mark": serializer.validated_data.get("mark"),
            "unit": serializer.validated_data.get("unit"),
            "mixChoices": serializer.validated_data.get("mixChoices")
        }
        questionSerializer = QuestionChangeSerializer(data = question_data)
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
        serializer = QuestionSerializer(instance=questions,data=request.data)
        if serializer.is_valid():
            serializer.save()
            response.data = serializer.data
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
        