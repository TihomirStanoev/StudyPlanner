from django.db import models
from django.utils import timezone
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


    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save(update_fields=['is_deleted', 'deleted_at', 'updated_at'])
        return 1, {self._meta.label: 1}


    def delete(self, *args, **kwargs):
        return self.soft_delete()


    def hard_delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)