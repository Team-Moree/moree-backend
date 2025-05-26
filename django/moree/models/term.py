import hashlib

from django.db import models
from django.utils.translation import gettext_lazy as _

from core.enums import StatusEnum
from moree.enums import TermAgreementTypeEnum


class Term(models.Model):
    term_category = models.ForeignKey(
        "moree.TermCategory",
        on_delete=models.RESTRICT,
        db_index=True
    )
    agreement_type = models.CharField(
        max_length=64,
        choices=TermAgreementTypeEnum.choices,
        default=TermAgreementTypeEnum.REQUIRED.value,
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
    )
    priority = models.PositiveSmallIntegerField(
        unique=True
    )
    status = models.CharField(
        max_length=64,
        choices=StatusEnum.choices,
        default=StatusEnum.INACTIVE.value,
        db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Term")
        verbose_name_plural = _("Terms")

    def save(self, *args, **kwargs):
        self.hash = hashlib.md5(self.content.encode()).hexdigest()
        super().save(*args, **kwargs)


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

