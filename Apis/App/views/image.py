from rest_framework import viewsets, mixins
from App.models import Image
from App.serializers import ImageDeleteSerializer, ImageSerializer, ImageValidate, ImageCreateSerializer, ImageMakeSerializer
from App.commons.response import ResponseReadMany, ResponseReadOne, ResponseCreateOne, ResponseDestroyOne
from App.commons.enum import ReponseEnum
from rest_framework.parsers import MultiPartParser
import uuid
class ImageView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
    ):
    queryset = Image.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return ImageMakeSerializer
        return ImageSerializer
    parser_classes = [MultiPartParser]

    def list(self, request, pk=None):
        images = Image.objects.filter(deletedAt__isnull=True).all()
        serializer = ImageSerializer(images, many=True)

        return ResponseReadMany(
            data=serializer.data,
            total_count=len(serializer.data)
        ).to_response()
    
    def retrieve(self, request, pk):
        messages = ImageValidate.run(pk, 'pk')
        response = ResponseReadOne()
        if len(messages) == 0:
            image = Image.objects.get(pk=pk)
            serializer = ImageSerializer(image)
            response.data=serializer.data,
        else:
            response.messages = messages
            response.status = ReponseEnum.BAD_REQUEST.value
            response.toast = True
        return response.to_response()
    
    def create(self, request):
        response = ResponseCreateOne()
        file = request.data.get("file")
        print(request.data)

        if not file:
            response.messages = ['Image file is required.']
            response.status = ReponseEnum.BAD_REQUEST.value
            response.toast = True
            return response.to_response()

        file_data = {
            "file": file,
            "type": file.content_type,
            "size": file.size,
            "original_name": file.name
        }

        serializer = ImageCreateSerializer(data=file_data)
        if serializer.is_valid():
            serializer.save()
            response.data = serializer.data
            response.toast = True
            response.status = ReponseEnum.SUCCESS.value
        else:
            response.messages = serializer.errors
            response.status = ReponseEnum.BAD_REQUEST.value

        return response.to_response() 
    
    def destroy(self, request, pk):
        messages = ImageValidate.run(pk, 'pk')
        response = ResponseDestroyOne()
        if len(messages) == 0:
            image = Image.objects.get(pk=pk)
            Image.delete(image)
            serializer = ImageDeleteSerializer(image)
            response.data=serializer.data,
            response.toast = True
        else:
            response.messages = messages
            response.status = ReponseEnum.BAD_REQUEST.value
            response.toast = True
        return response.to_response()
        