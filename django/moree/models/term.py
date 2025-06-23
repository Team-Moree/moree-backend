from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel
from moree.enums import TermAgreementTypeEnum


class Term(BaseModel):
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

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Term")
        verbose_name_plural = _("Terms")


class TermCategory(BaseModel):
    name = models.CharField(
        max_length=255
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Term Category")
        verbose_name_plural = _("Term Categories")
