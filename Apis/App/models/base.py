from django.db import models
from django.utils import timezone

class Base(models.Model):
    isFreeze = models.BooleanField(null=False, default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    deletedAt = models.DateTimeField(null=True, blank=True, default=None)
    isFreeze = models.BooleanField(default=False)
    isActivate = models.BooleanField(default=True)
    
    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.deletedAt = timezone.now()
        self.save()