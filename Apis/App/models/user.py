from django.db import models
from .profiling import Profiling
from .password import Password
from .role import Role
from .base import Base
from .subject import Subject
import uuid

class User(Base):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    isActivate = models.BooleanField(null=False, default=False)
    username = models.CharField(max_length=50, unique=True, null=False)
    password = models.OneToOneField(Password, on_delete=models.CASCADE, null=False)
    profiling = models.OneToOneField(Profiling, on_delete=models.CASCADE, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    subject = models.ManyToManyField(Subject, related_name='subjects')