from django.db import models
from .base import Base
import uuid

class Password(Base):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hash = models.TextField(null=False)