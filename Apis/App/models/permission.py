from django.db import models
from .base import Base
import uuid

class Permission(Base):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50,null=False, default=False)