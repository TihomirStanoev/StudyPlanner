from django.db import models
from django.utils import timezone


class SoftDeletionQuerySet(models.QuerySet):
    def delete(self, *args, **kwargs):
        return self.update(is_deleted=True, deleted_at = timezone.now())

    def hard_delete(self):
        return super().delete()


class SoftDeletionManager(models.Manager):
    def get_queryset(self) -> SoftDeletionQuerySet:
        return SoftDeletionQuerySet(self.model, using=self._db).filter(is_deleted=False)

    def hard_delete(self):
        return self.get_queryset().hard_delete()
