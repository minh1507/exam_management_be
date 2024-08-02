from rest_framework import viewsets, mixins
from App.models import Image
from App.serializers import ImageDeleteSerializer, ImageSerializer, ImageValidate, ImageCreateSerializer
from App.commons.response import ResponseReadMany, ResponseReadOne, ResponseCreateOne, ResponseDestroyOne
from App.commons.enum import ReponseEnum
from rest_framework.parsers import MultiPartParser

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
            return ImageCreateSerializer
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
        messages = ImageValidate.run(request.data, 'create')
        response = ResponseCreateOne()

        serializer = ImageSerializer(data=request.data)

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
        messages = ImageValidate.run(request.data, 'create', pk) + ImageValidate.run(pk, 'pk')
        response = ResponseCreateOne()
        if(len(messages) > 0):
            response.messages = messages
            response.status = ReponseEnum.BAD_REQUEST.value
            response.toast = True
            return response.to_response() 
        
        images = Image.objects.get(pk=pk)
        serializer = ImageSerializer(instance=images,data=request.data)
        if serializer.is_valid():
            serializer.save()
            response.data = serializer.data
            response.toast = True
            response.status = ReponseEnum.SUCCESS.value
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
        