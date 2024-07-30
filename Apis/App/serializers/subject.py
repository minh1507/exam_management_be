from rest_framework import serializers
from App.models.subject import Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'code']

class SubjectDeleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'deletedAt')
                
class ProjectValidate():
    def run(data):
        messages = MessageUtil()
        if data.get('name') is None or data.get('name') == "":
            messages.push(ContentMessage.REQUIRED.value, KeyMessage.NAME.value)
        if data.get('code') is None or data.get('code') == "":
            messages.push(ContentMessage.REQUIRED.value, KeyMessage.CODE.value)
        if len(data.get('code')) > 15:
            message.push(ContentMessage.INVALID_CODE.value, KeyMessage.CODE.value)
        if Subject.objects.filter(code=value.get('code')).exists():
            messages.push(ContentMessage.EXISTED.value, KeyMessage.CODE.value)
        return messages.get()

class ProjectCreateSerializer(serializer.Serializer):
    name = serializer.CharField(max_length=100)
    code serializer.CharField(max_length=20)

    def to_data(self):
        return self.data