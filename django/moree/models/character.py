from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel


class Character(BaseModel):
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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Character")
        verbose_name_plural = _("Characters")
