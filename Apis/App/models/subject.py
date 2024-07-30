from django.db import models
from .base import Base
import uuid

class Subject(Base):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    isActivate = models.BooleanField(null=False, default=False)
    code = models.CharField(max_length=20, unique=True, null=False)
    name = models.CharField(max_length=100, null=True)