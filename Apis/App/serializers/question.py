from rest_framework import serializers
from App.models.subject import Subject
from App.models.question import Question
from App.commons.message import KeyMessage, ContentMessage
from App.commons.util import MessageUtil
from App.commons.util import StringUtil
from .subject import SubjectSerializer

class QuestionSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    class Meta:
        model = Question
        fields = ('id', 'subject', 'lecturer', 'question', "mark", "unit", "mixChoices", "imageId"
         )

class QuestionDeleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'deletedAt')

class QuestionValidate():
    def checkRequire(value, field, *message):
        if value.get(field) is None or value.get(field) == "":
            message.push(ContentMessage.REQUIRED.value, KeyMessage.field.value)

    def checkInvalid(value, field, *message):
        if value.get(field) is None or value.get(field) == "":
            message.push(ContentMessage.INVALID.value, KeyMessage.field.value)

    def run(self, value, type, id=None):
        messages = MessageUtil()
        match type:
            case "create":
                self.checkRequire(value, 'code', messages)
                self.checkRequire(value, 'question', messages)
                self.checkRequire(value, 'mark', messages)
                return messages.get()
            case "update":
                self.checkRequire(value, 'code', messages)
                return messages.get()
            case "pk":
                if value.isnumeric() == True:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.ID.value)
                if StringUtil.is_valid_uuid(value) == False:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.ID.value)
                return messages.get()

class QuestionCreateSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=50)
    subjectCode = serializers.CharField(max_length=50)
    lecturer = serializers.CharField(max_length=100)
    question = serializers.CharField(max_length=50)
    mark = serializers.FloatField()
    unit = serializers.CharField(max_length=50)
    mixChoices = serializers.BooleanField()
    imageId = serializers.CharField(max_length=50)