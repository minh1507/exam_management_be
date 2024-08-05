from rest_framework import serializers
from App.models.exam import Exam
from .subject import SubjectSerializer
from App.models.subject import Subject
from App.models.question import Question
from App.models.answer import Answer
from App.commons.util.message import MessageUtil
from App.commons.message.content import ContentMessage
from App.commons.message.key import KeyMessage
from App.commons.util.string import StringUtil
from .image import ImageSerializer

class AnswerForQuestionMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'content', "isResult"] 

class QuestionExamMakeSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    image = ImageSerializer()
    answers = AnswerForQuestionMakeSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ('id', 'subject', 'lecturer', 'content', "mark", "unit", "mixChoices", "image", 'answers')

class ExamSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    questions = QuestionExamMakeSerializer(many=True)
    class Meta:
        model = Exam
        fields = ('id', 'code', "subject", 'supervisor', 'expired_time', 
                  'start_time','total_question', 'questions'
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
            

class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = (
            "id",
            )
    
class ExamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['subject', 'expired_time', 'start_time', 'total_question', 'supervisor', 'code']

    def create(self, validated_data):
        return Exam.objects.create(**validated_data)
    
class ExamCreateManySerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all(), many=True)
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
    class Meta:
        model = Exam
        fields = ['questions', 'code', 'supervisor', 'expired_time', 'start_time', 'total_question', 'subject']

    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        exam = Exam.objects.create(**validated_data)
        exam.questions.set(questions_data)
        return exam
    
    def to_data(self):
            return self.data
    

