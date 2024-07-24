from django.db import models
from .base import Base

class Ethnic(Base) :
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    code = models.CharField(max_length=50, null=False)