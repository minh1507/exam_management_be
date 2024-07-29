from rest_framework import viewsets, mixins
from App.models import Ethnic
from App.serializers import EthnicSerializer, EthnicValidate, EthnicDeleteSerializer
from App.commons.response import ResponseReadMany, ResponseReadOne, ResponseCreateOne, ResponseDestroyOne, ResponseBadRequest
from App.commons.enum import ReponseEnum
class RoleView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
    ):
    queryset = Ethnic.objects.all()
    serializer_class = EthnicSerializer

    def list(self, request, pk=None):
        ethnics = Ethnic.objects.all()
        serializer = EthnicSerializer(ethnics, many=True)

        return ResponseReadMany(
            data=serializer.data,
            total_count=len(serializer.data)
        ).to_response()
    
    def retrieve(self, request, pk):
        messages = EthnicValidate.run(pk, 'pk')
        response = ResponseReadOne()
        if len(messages) == 0:
            ethnic = Ethnic.objects.get(pk=pk)
            serializer = EthnicSerializer(ethnic)
            response.data=serializer.data,
        else:
            response.messages = messages
            response.status = ReponseEnum.BAD_REQUEST.value
            response.toast = True
        return response.to_response()
    
    def create(self, request):
        messages = EthnicValidate.run(request.data, 'create')
        response = ResponseCreateOne()

        serializer = EthnicSerializer(data=request.data)

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
        messages = EthnicValidate.run(request.data, 'create') + EthnicValidate.run(pk, 'pk')
        response = ResponseCreateOne()
        if(len(messages) > 0):
            response.messages = messages
            response.status = ReponseEnum.BAD_REQUEST.value
            response.toast = True
            return response.to_response() 
        
        ethnics = Ethnic.objects.get(pk=pk)
        serializer = EthnicSerializer(instance=ethnics,data=request.data)
        if serializer.is_valid():
            serializer.save()
            response.data = serializer.data
            response.toast = True
        return response.to_response() 
    
    def destroy(self, request, pk):
        messages = EthnicValidate.run(pk, 'pk')
        response = ResponseDestroyOne()
        if len(messages) == 0:
            ethnic = Ethnic.objects.get(pk=pk)
            Ethnic.delete(ethnic)
            serializer = EthnicDeleteSerializer(ethnic)
            response.data=serializer.data,
            response.toast = True
        else:
            response.messages = messages
            response.status = ReponseEnum.BAD_REQUEST.value
            response.toast = True
        return response.to_response()
        