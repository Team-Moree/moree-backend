from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel


class Store(BaseModel):
    store_categories = models.ManyToManyField(
        "moree.StoreCategory",
    )
    # TODO: 등록한 유저에 대한 정보 필요
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=7
    )
    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=7
    )
    description = models.TextField()
    business_day = models.PositiveSmallIntegerField(
        default=127,
        help_text="day of the week, bitmask (127=01111111=all days)"
    )
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    profile_img_stored_files_group = models.ForeignKey(
        "common.StoredFilesGroup",
        on_delete=models.CASCADE
    )
    pre_order_start_at = models.DateTimeField(
        default=None,
        null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Store")
        verbose_name_plural = _("Stores")


class StoreCategory(BaseModel):
    name = models.CharField(
        max_length=64,
        unique=True
    )
    priority = models.PositiveSmallIntegerField(
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Store Category")
        verbose_name_plural = _("Store Categories")


class StoreCharacterPool(BaseModel):
    store = models.ForeignKey(
        "moree.Store",
        on_delete=models.CASCADE,
        db_index=True
    )
    character = models.ForeignKey(
        "moree.Character",
        on_delete=models.CASCADE,
        db_index=True
    )
    weight = models.PositiveIntegerField(
        help_text="뽑힐 가중치 (값이 클수록 잘 뽑힘)"
    )

    class Meta:
        verbose_name = _("Store Character Pool")
        verbose_name_plural = _("Store Character Pools")
