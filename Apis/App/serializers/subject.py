from rest_framework import serializers
from App.models.subject import Subject
from App.commons.message import KeyMessage, ContentMessage
from App.commons.util import MessageUtil
from App.commons.util import StringUtil
class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name', 'code', 'order')

class SubjectDeleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'deletedAt')

class SubjectValidate():
    def run(value, type, id=None):
        messages = MessageUtil()
        match type:
            case "create":
                if value.get('name') is None or value.get('name') == "":
                    messages.push(ContentMessage.REQUIRED.value, KeyMessage.NAME.value)
                if value.get('name') is not None and (value.get('name')).isnumeric() == True:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.NAME.value)
                if value.get('code') is None or value.get('code') == "":
                    messages.push(ContentMessage.REQUIRED.value, KeyMessage.CODE.value)
                if value.get('code') is not None and (value.get('code')).isnumeric() == True:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.CODE.value)
                if Subject.objects.filter(code=value.get('code')).exists():
                    messages.push(ContentMessage.EXISTED.value, KeyMessage.CODE.value)
                if value.get('order') is None or value.get('order') == "":
                    messages.push(ContentMessage.REQUIRED.value, KeyMessage.ORDER.value)
                if value.get('order') is not None and (str(value.get('order'))).isnumeric() == False:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.ORDER.value)
                return messages.get()
            case "update":
                if value.get('name') is None or value.get('name') == "":
                    messages.push(ContentMessage.REQUIRED.value, KeyMessage.NAME.value)
                if value.get('name') is not None and (value.get('name')).isnumeric() == True:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.NAME.value)
                if value.get('code') is None or value.get('code') == "":
                    messages.push(ContentMessage.REQUIRED.value, KeyMessage.CODE.value)
                if value.get('code') is not None and (value.get('code')).isnumeric() == True:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.CODE.value)
                if Subject.objects.filter(name=value.get('code')).exclude(id=id).exists():
                    messages.push(ContentMessage.EXISTED.value, KeyMessage.CODE.value)
                if value.get('order') is None or value.get('order') == "":
                    messages.push(ContentMessage.REQUIRED.value, KeyMessage.ORDER.value)
                if value.get('order') is not None and (str(value.get('order'))).isnumeric() == False:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.ORDER.value)
                return messages.get()
            case "pk":
                if value.isnumeric() == True:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.ID.value)
                if StringUtil.is_valid_uuid(value) == False:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.ID.value)
                return messages.get()
                
        