from django.db import models
from .base import Base
from .subject import Subject
from .question import Question
import uuid

class Exam(Base):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=50, unique=True, null=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    questions = models.ManyToManyField(Question, related_name='questions')
    supervisor = models.CharField(max_length = 100, null = True)
    expiredTime = models.DateTimeField()
    startTime = models.DateTimeField(auto_now_add=True)
    sumQuestion = models.IntegerField()