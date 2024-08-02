from rest_framework import serializers
from App.models.image import Image
from App.commons.message import KeyMessage, ContentMessage
from App.commons.util import MessageUtil
from App.commons.util import StringUtil

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', "origin_name", "mime_type", "size", "target", "path")

class ImageDeleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'deletedAt')

class ImageValidate():
    def run(value, type, id=None):
        messages = MessageUtil()
        match type:
            case "create":
                # if Subject.objects.filter(id=value.get('subject')).exists() == False:
                #     messages.push(ContentMessage.NOT_EXISTED.value, KeyMessage.SUBJECT.value)
                # if value.get('content') is None or value.get('content') == "":
                #     messages.push(ContentMessage.REQUIRED.value, KeyMessage.CONTENT.value)
                # if value.get('mark') is None or value.get('mark') == "":
                #     messages.push(ContentMessage.REQUIRED.value, KeyMessage.MARK.value)
                return messages.get()
            case "pk":
                if value.isnumeric() == True:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.ID.value)
                if StringUtil.is_valid_uuid(value) == False:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.ID.value)
                return messages.get()

class ImageCreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Image
        fields = ['image']
