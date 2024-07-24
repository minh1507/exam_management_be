from django.db import models
from .base import Base

class Password(Base):
    id = models.AutoField(primary_key=True)
    hash = models.CharField(max_length=60, null=False)