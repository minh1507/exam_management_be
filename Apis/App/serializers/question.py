from rest_framework import serializers
from App.models.subject import Subject
from App.models.question import Question
from App.commons.message import KeyMessage, ContentMessage
from App.commons.util import MessageUtil
from App.commons.util import StringUtil
from .subject import SubjectSerializer
from .image import ImageSerializer

class QuestionSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    image = ImageSerializer()
    class Meta:
        model = Question
        fields = ('id', 'subject', 'lecturer', 'content', "mark", "unit", "mixChoices", "image")

class QuestionDeleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'deletedAt')

class QuestionValidate():
    def run(value, type, id=None):
        messages = MessageUtil()
        match type:
            case "create":
                if Subject.objects.filter(id=value.get('subject')).exists() == False:
                    messages.push(ContentMessage.NOT_EXISTED.value, KeyMessage.SUBJECT.value)
                if value.get('content') is None or value.get('content') == "":
                    messages.push(ContentMessage.REQUIRED.value, KeyMessage.CONTENT.value)
                if value.get('mark') is None or value.get('mark') == "":
                    messages.push(ContentMessage.REQUIRED.value, KeyMessage.MARK.value)
                return messages.get()
            case "pk":
                if value.isnumeric() == True:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.ID.value)
                if StringUtil.is_valid_uuid(value) == False:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.ID.value)
                return messages.get()

class QuestionCreateSerializer(serializers.ModelSerializer):
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
    class Meta:
        model = Question
        fields = ['subject', 'lecturer', 'content', 'mark', 'unit', 'mixChoices']

    def create(self, validated_data):
        return Question.objects.create(**validated_data)