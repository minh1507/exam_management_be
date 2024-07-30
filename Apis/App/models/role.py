from django.db import models
from .base import Base
import uuid

class Role(Base):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50,null=False, default=False)
    code = models.CharField(max_length=50,null=False, default=False, unique=True)