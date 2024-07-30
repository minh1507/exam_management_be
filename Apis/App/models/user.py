from django.db import models
from .profile import Profile
from .password import Password
from .role import Role
from .base import Base
import uuid

class User(Base):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    isActivate = models.BooleanField(null=False, default=False)
    username = models.CharField(max_length=50, unique=True, null=False)
    password = models.OneToOneField(Password, on_delete=models.CASCADE, null=False)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)