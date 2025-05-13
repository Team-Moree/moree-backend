from django.db import models
from django.utils.translation import gettext_lazy as _

from core.enums import StatusEnum


class Character(models.Model):
    # TODO : 이름 변경
    name = models.CharField(
        max_length=255,
        db_index=True
    )
    profile_img_stored_file = models.ForeignKey(
        "common.StoredFile",
        on_delete=models.CASCADE,
        null=True,
        default=None
    )
    description = models.TextField()
    status = models.CharField(
        max_length=64,
        choices=StatusEnum.choices,
        default=StatusEnum.ACTIVE.value
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Character")
        verbose_name_plural = _("Characters")
