from rest_framework import serializers
from App.models.subject import Subject
from App.models.question import Question
from App.commons.message import KeyMessage, ContentMessage
from App.commons.util import MessageUtil
from App.commons.util import StringUtil
from .subject import SubjectSerializer

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    subject = SubjectSerializer()
    class Meta:
        model = Question
        fields = ('id', 'subject', 'code', 'lecturer', 'question', 'ansA', 'ansB',
         'ansC', 'ansD', "answer", "mark", "unit", "mixChoices"
         )

class QuestionDeleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'deletedAt')

class QuestionValidate():
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
                checkRequire(value, 'code', message)
                checkRequire(value, 'question', message)
                checkRequire(value, 'ansA', message)
                checkRequire(value, 'ansB', message)
                checkRequire(value, 'answer', message)
                checkRequire(value, 'mark', message)
                checkRequire(value, 'unit', message)
                return messages.get()
            case "update":
                checkRequire(value, 'code', message)
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
    question = serializers.CharField()
    ansA = serializers.CharField()
    ansB = serializers.CharField()
    ansC = serializers.CharField()
    ansD = serializers.CharField()
    answer = serializers.CharField(max_length=10)
    mark = serializers.FloatField()
    unit = serializers.CharField(max_length=50)
    mixChoices = serializers.BooleanField()

    def to_data(self):
            return self.data    


class QuestionChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['code', 'subject', 'lecturer', 'question', 'ansA', 'ansB',
         'ansC', 'ansD', "answer", "mark", "unit", "mixChoices"]  