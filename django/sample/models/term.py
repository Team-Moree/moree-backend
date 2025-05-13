import hashlib

from django.db import models
from django.utils.translation import gettext_lazy as _

from core.enums import StatusEnum


class Term(models.Model):
    term_category = models.ForeignKey(
        "sample.TermCategory",
        on_delete=models.RESTRICT,
        db_index=True
    )
    name = models.CharField(
        max_length=255
    )
    content = models.TextField()
    version = models.CharField(
        max_length=64,
        db_index=True
    )
    hash = models.CharField(
        max_length=255,
        db_index=True,
        editable=False,
        default=None
        # default=lambda: hashlib.md5(binary).hexdigest()
    )
    status = models.CharField(
        max_length=64,
        choices=StatusEnum.choices,
        default=StatusEnum.INACTIVE.value,
        db_index=True
    )
    priority = models.PositiveSmallIntegerField(
        unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Term")
        verbose_name_plural = _("Terms")


class TermCategory(models.Model):
    name = models.CharField(
        max_length=255
    )
    status = models.CharField(
        max_length=64,
        choices=StatusEnum.choices,
        default=StatusEnum.ACTIVE.value,
        db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Term Category")
        verbose_name_plural = _("Term Categories")

