from rest_framework import serializers
from App.models.answer import Answer, Question
from .question import QuestionSerializer
from App.commons.message import KeyMessage, ContentMessage
from App.commons.util import MessageUtil
from App.commons.util import StringUtil

class AnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()
    class Meta:
        model = Answer
        fields = ('id', 'question', 'content', 'isResult')


class AnswerDeleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'deletedAt')

class AnswerValidate():
    def run(value, type, id=None):
        messages = MessageUtil()
        match type:
            case "create":
                if Question.objects.filter(id=value.get('question')).exists() == False:
                    messages.push(ContentMessage.NOT_EXISTED.value, KeyMessage.SUBJECT.value)
                if value.get('content') is None or value.get('content') == "":
                    messages.push(ContentMessage.REQUIRED.value, KeyMessage.CONTENT.value)
                return messages.get()
            case "pk":
                if value.isnumeric() == True:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.ID.value)
                if StringUtil.is_valid_uuid(value) == False:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.ID.value)
                return messages.get()

class AnswerCreateSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())
    class Meta:
        model = Answer
        fields = ['question', 'content', 'isResult']

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)

                
        