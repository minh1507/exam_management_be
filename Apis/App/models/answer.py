from django.db import models
from .base import Base
import uuid
from .question import Question

class Answer(Base):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, related_name='answers')
    content = models.TextField()
    isResult = models.BooleanField()