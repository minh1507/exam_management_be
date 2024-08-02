from rest_framework import serializers
from App.models.exam import Exam

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ('id', 'code')
