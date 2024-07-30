from django.db import models
from .base import Base
import uuid

class Question(Base):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=50, unique=True, null=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null = False)
    lecturer = models.CharField(max_length=100, null=True)
    question = models.TextField()
    ansA = models.TextField()
    ansB = models.TextField()
    ansC = models.TextField()
    ansD = models.TextField()
    answer = models.CharField(max_length=10, null=False)
    mark = models.FloatField()
    unit = models.CharField(max_length=50)
    mixChoices = models.BooleanField(default=True)
