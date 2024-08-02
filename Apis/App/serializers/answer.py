from rest_framework import serializers
from App.models.answer import Answer
from .question import QuestionSerializer

class AnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()
    class Meta:
        model = Answer
        fields = ('id', 'question', 'content', 'isResult')


class AnswerDeleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'deletedAt')

class AnswerValidate():
    def checkRequire(value, field, *message):
        if value.get(field) is None or value.get(field) == "":
            messages.push(ContentMessage.REQUIRED.value, KeyMessage.field.value)

    def checkInvalid(value, field, *message):
        if value.get(field) is None or value.get(field) == "":
            messages.push(ContentMessage.INVALID.value, KeyMessage.field.value)

    def run(value, type, id=None):
        messages = MessageUtil()
        match type:
            case "create":
                checkRequire(value, 'content', message)
                checkRequire(value, 'question', message)
                return messages.get()
            case "update":
                checkRequire(value, 'content', message)
                return messages.get()
            case "pk":
                if value.isnumeric() == True:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.ID.value)
                if StringUtil.is_valid_uuid(value) == False:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.ID.value)
                return messages.get()

class AnswerCreateSerializer(serializers.Serializer):
    questionId = serializers.CharField(max_length=50)
    content = serializers.CharField()
    isResult = serializers.BooleanField()

                
        