from django.db import models
from .base import Base
import uuid

class Role(Base):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=False, default=False)