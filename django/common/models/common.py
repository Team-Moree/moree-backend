import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from core.environment import env
from core.enums import StatusEnum
from lib.timestamp import Timestamp

from common.enums import UploaderTypeEnum


class StoredFile(models.Model):
    stored_files_group = models.ForeignKey(
        "common.StoredFilesGroup",
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        db_index=True,
        default=None
    )
    name = models.CharField(
        max_length=255,
        db_index=True
    )
    ext = models.CharField(
        max_length=255,
        db_index=True
    )
    path = models.CharField(
        max_length=255,
        db_index=True
    )
    status = models.CharField(
        max_length=64,
        db_index=True,
        choices=StatusEnum.choices,
        default=StatusEnum.ACTIVE.value,
    )
    hash = models.CharField(
        max_length=255,
        db_index=True,
        editable=False,
        default=StatusEnum.INACTIVE.value
    )
    uploader_type = models.CharField(
        max_length=64,
        db_index=True,
        choices=UploaderTypeEnum.choices,
        default=UploaderTypeEnum.ADMIN.value,
    )
    uploader_id = models.PositiveIntegerField(
        db_index=True
    )
    priority = models.PositiveSmallIntegerField(
        default=0
    )
    expire_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}{self.ext}"

    class Meta:
        verbose_name = _("Stored File")
        verbose_name_plural = _("Stored Files")

    def delete(self, using=None, keep_parents=False):
        self.expire_at = (Timestamp() + int(env.get("STATIC_FILE_EXPIRE_TIME"))).datetime
        self.status = StatusEnum.INACTIVE.value
        self.save()


class StoredFilesGroup(models.Model):
    name = models.CharField(
        max_length=255,
        default=uuid.uuid4
    )
    description = models.TextField(null=True)
    status = models.CharField(
        max_length=64,
        db_index=True,
        choices=StatusEnum.choices,
        default=StatusEnum.ACTIVE.value
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Stored File Group")
        verbose_name_plural = _("Stored Files Groups")

    def delete(self, using=None, keep_parents=False):
        self.status = StatusEnum.INACTIVE.value
        self.save()
