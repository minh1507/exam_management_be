from django.db import models
from .base import Base

class Profile(Base):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=10, null=False)
    lastname = models.CharField(max_length=10, null=False)
    middlename = models.CharField(max_length=10, null=False)
    email = models.CharField(max_length=50, unique=True, null=False)
    age = models.PositiveIntegerField(null=True)