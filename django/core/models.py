from django.db import models

from lib.timestamp import Timestamp


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        db_index=True,
    )

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = Timestamp().datetime
        self.save()

    class Meta:
        abstract = True


__all__ = ("BaseModel",)
