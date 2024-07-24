from rest_framework import serializers
from App.models.ethnic import Ethnic
from App.commons.message import KeyMessage, ContentMessage
from App.commons.util import MessageUtil

class EthnicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ethnic
        fields = ('id', 'name', 'code')

class EthnicValidate():
    def run(value):
        messages = MessageUtil()
        if value.get('name') is None:
            messages.push(ContentMessage.REQUIRED.value, KeyMessage.NAME.value)
        if Ethnic.objects.filter(name=value.get('name')).exists():
            messages.push(ContentMessage.EXISTED.value, KeyMessage.NAME.value)
        return messages.get()