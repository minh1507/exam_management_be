from ..serializers.ethnic import EthnicSerializer
from ..models.ethnic import Ethnic
from rest_framework.decorators import api_view
from ..models.ethnic import Ethnic
from App.commons.response.read import ResponseRead

class EthnicView:
    @api_view(['GET'])
    def find_all(request):
        ethnics = Ethnic.objects.all()
        serializer = EthnicSerializer(ethnics, many=True)

        response = ResponseRead(
            data=serializer.data,
            total_count=len(serializer.data)
        )
        return response.to_response()
    
    @api_view(['GET'])
    def find_one(request, pk):
        print(1)
        # ethnic = Ethnic.objects.get(pk=pk)

        # serializer = EthnicSerializer(ethnic)
        # return Response(serializer.data)