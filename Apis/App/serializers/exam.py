from rest_framework import serializers
from App.models.exam import Exam

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name', 'code')
