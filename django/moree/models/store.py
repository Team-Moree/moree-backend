from django.db import models
from django.utils.translation import gettext_lazy as _

from core.enums import StatusEnum


class Store(models.Model):
    store_categories = models.ManyToManyField(
        "moree.StoreCategory",
    )
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
    status = models.CharField(
        max_length=64,
        choices=StatusEnum.choices,
        default=StatusEnum.INACTIVE.value
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Store")
        verbose_name_plural = _("Stores")


class StoreCategory(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True
    )
    priority = models.PositiveSmallIntegerField(
        unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Store Category")
        verbose_name_plural = _("Store Categories")


class StoreCharacterPool(models.Model):
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
    status = models.CharField(
        max_length=64,
        choices=StatusEnum.choices,
        default=StatusEnum.ACTIVE.value,
        db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Store Character Pool")
        verbose_name_plural = _("Store Character Pools")
