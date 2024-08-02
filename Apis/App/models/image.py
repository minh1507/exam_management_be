from django.db import models
from .base import Base
import uuid

class Image(Base):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    origin_name = models.CharField(max_length=100)
    mime_type = models.CharField(max_length=50)
    size = models.IntegerField()
    target = models.CharField(max_length=100)
    path = models.CharField(max_length=100)