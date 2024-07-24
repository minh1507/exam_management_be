from rest_framework import viewsets
from App.models.ethnic import Ethnic
from App.serializers.ethnic import EthnicSerializer, EthnicValidate
from App.commons.response import ResponseReadMany, ResponseReadOne, ResponseCreateOne
from App.commons.enum import ReponseEnum

class EthnicView(viewsets.ModelViewSet):
    serializer_class = EthnicSerializer

    def list(self, request, pk=None):
        ethnics = Ethnic.objects.all()
        serializer = EthnicSerializer(ethnics, many=True)
        response = ResponseReadMany(
            data=serializer.data,
            total_count=len(serializer.data)
        )
        return response.to_response()
    
    # def find_one(request, pk):
    #     ethnic = Ethnic.objects.get(pk=pk)
    #     serializer = GetEthnicSerializer(ethnic)
    #     response = ResponseReadOne(
    #         data=serializer.data,
    #     )
    #     return response.to_response()
    
    def create(self, request):
        serializer = EthnicSerializer(data=request.data)
        messages = EthnicValidate.run(request.data)

        response = ResponseCreateOne(
            data=request.data,
            toast=True
        )

        if serializer.is_valid() and len(messages)==0:
            serializer.save()
        else:
            response.message = messages
            response.status = ReponseEnum.BAD_REQUEST.value
            
        return response.to_response()  
        