from rest_framework import serializers
from App.models.exam import Exam
from .question import QuestionSerializer
from .subject import SubjectSerializer
from App.models.subject import Subject

class ExamSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer()
    subject = SubjectSerializer()
    class Meta:
        model = Exam
        fields = ('id', 'code', "subject", 'questions', 'supervisor', 'expiredTime', 
                  'startTime','sumQuestion'
                  )
class ExamDeleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exam
        fields = ('id', 'deletedAt')

class ExamValidate():
    def run(value, type, id=None):
        messages = MessageUtil()
        match type:
            case "create":
                if Exam.objects.filter(id=value.get('code')).exists() == False:
                    messages.push(ContentMessage.NOT_EXISTED.value, KeyMessage.SUBJECT.value)
                if value.get('sumQuestion') is None or value.get('sumQuestion') == "":
                    messages.push(ContentMessage.REQUIRED.value, KeyMessage.CONTENT.value)
                return messages.get()
            case "pk":
                if value.isnumeric() == True:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.ID.value)
                if StringUtil.is_valid_uuid(value) == False:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.ID.value)
                return messages.get()
            

class ExamCreateSerializer(serializers.ModelSerializer):
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
    class Meta:
        model = Exam
        fields = ['subject', 'expiredTime', 'startTime', 'sumQuestion']

    def create(self, validated_data):
        return Exam.objects.create(**validated_data)

