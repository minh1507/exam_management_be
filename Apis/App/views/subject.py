from rest_framework import viewsets, mixins
from App.models import Subject
from App.serializers import SubjectSerializer, SubjectValidate, SubjectDeleteSerializer
from App.commons.response import ResponseReadMany, ResponseReadOne, ResponseCreateOne, ResponseDestroyOne
from App.commons.enum import ReponseEnum
class SubjectView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
    ):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def list(self, request, pk=None):
        subjects = Subject.objects.filter(deletedAt__isnull=True).all()
        serializer = SubjectSerializer(subjects, many=True)

        return ResponseReadMany(
            data=serializer.data,
            total_count=len(serializer.data)
        ).to_response()
    
    def retrieve(self, request, pk):
        messages = SubjectValidate.run(pk, 'pk')
        response = ResponseReadOne()
        if len(messages) == 0:
            subject = Subject.objects.get(pk=pk)
            serializer = SubjectSerializer(subject)
            response.data=serializer.data,
        else:
            response.messages = messages
            response.status = ReponseEnum.BAD_REQUEST.value
            response.toast = True
        return response.to_response()
    
    def create(self, request):
        messages = SubjectValidate.run(request.data, 'create')
        response = ResponseCreateOne()

        serializer = SubjectSerializer(data=request.data)

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
        messages = SubjectValidate.run(request.data, 'update', pk) + SubjectValidate.run(pk, 'pk')
        response = ResponseCreateOne()
        if(len(messages) > 0):
            response.messages = messages
            response.status = ReponseEnum.BAD_REQUEST.value
            response.toast = True
            return response.to_response() 
        
        subjects = Subject.objects.get(pk=pk)
        serializer = SubjectSerializer(instance=subjects,data=request.data)
        if serializer.is_valid():
            serializer.save()
            response.data = serializer.data
            response.toast = True
            response.status = ReponseEnum.SUCCESS.value
        return response.to_response() 
    
    def destroy(self, request, pk):
        messages = SubjectValidate.run(pk, 'pk')
        response = ResponseDestroyOne()
        if len(messages) == 0:
            subject = Subject.objects.get(pk=pk)
            Subject.delete(subject)
            serializer = SubjectDeleteSerializer(subject)
            response.data=serializer.data,
            response.toast = True
        else:
            response.messages = messages
            response.status = ReponseEnum.BAD_REQUEST.value
            response.toast = True
        return response.to_response()
        