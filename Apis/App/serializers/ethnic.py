from rest_framework import serializers
from App.models.ethnic import Ethnic
from App.commons.message import KeyMessage, ContentMessage
from App.commons.util import MessageUtil
from App.commons.util import StringUtil
class EthnicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ethnic
        fields = ('id', 'name', 'code')

class EthnicDeleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ethnic
        fields = ('id', 'deletedAt')

class EthnicValidate():
    def run(value, type):
        messages = MessageUtil()
        match type:
            case "create":
                if value.get('name') is None or value.get('name') == "":
                    messages.push(ContentMessage.REQUIRED.value, KeyMessage.NAME.value)
                if value.get('name') is not None and (value.get('name')).isnumeric() == True:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.NAME.value)
                if Ethnic.objects.filter(name=value.get('name')).exists():
                    messages.push(ContentMessage.EXISTED.value, KeyMessage.NAME.value)
                if value.get('code') is None or value.get('code') == "":
                    messages.push(ContentMessage.REQUIRED.value, KeyMessage.CODE.value)
                if value.get('code') is not None and (value.get('code')).isnumeric() == True:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.CODE.value)
                return messages.get()
            case "pk":
                if value.isnumeric() == True:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.ID.value)
                if StringUtil.is_valid_uuid(value) == False:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.ID.value)
                return messages.get()
                
        