from django.db import models
from .base import Base
import uuid
from django_minio_backend import MinioBackend, iso_date_prefix
from App.commons.util.string import StringUtil

class Image(Base):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=10, null=True)
    original_name = models.CharField(max_length=100, null=True)
    size = models.BigIntegerField(null=True)
    file = models.FileField(storage=MinioBackend(bucket_name='exam'), upload_to=StringUtil.get_uuid_filename)