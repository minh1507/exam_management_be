from django.db import models
from .base import Base
from .subject import Subject
import uuid

class Question(Base):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null = False)
    lecturer = models.CharField(max_length=100, null=True)
    content = models.TextField()
    mark = models.FloatField()
    unit = models.CharField(max_length=50)
    mixChoices = models.BooleanField(default=True)
    imageId = models.CharField(max_length=50)