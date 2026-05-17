from django.db import models

from common.managers import SoftDeletionManager


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class SoftDeletionModel(BaseModel):
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)


    objects = SoftDeletionManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True
