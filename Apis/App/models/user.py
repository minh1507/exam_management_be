from django.db import models
from .profile import Profile
from .password import Password
from .ethnic import Ethnic
from .base import Base

class User(Base):
    id = models.AutoField(primary_key=True)
    isActivate = models.BooleanField(null=False, default=False)
    username = models.CharField(max_length=10, unique=True, null=False)
    password = models.OneToOneField(Password, on_delete=models.CASCADE, null=False)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)
    ethnic = models.OneToOneField(Ethnic, on_delete=models.CASCADE, null=True)