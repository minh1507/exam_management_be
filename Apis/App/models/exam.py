from django.db import models
from .base import Base
from .subject import Subject
from .question import Question
import uuid

class Exam(Base):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=50, unique=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    questions = models.ManyToManyField(Question, related_name='questions')
    supervisor = models.CharField(max_length = 100, null = True)
    expired_time = models.DateTimeField( null=True)
    start_time = models.DateTimeField(null=True)
    total_question = models.IntegerField( null=True)