from django.db import models
from .base import Base
from .subject import Subject
import uuid

class Exam(Base):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=50, unique=True, null=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null = False)
    questions = models.CharField(max_length=200, null = False)
    sumQuestion = models.IntegerField()
    totalMark = models.FloatField()