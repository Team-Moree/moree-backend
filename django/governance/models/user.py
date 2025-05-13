import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from core.environment import env
from lib.timestamp import Timestamp
from lib.functions import get_random_string

from governance.enums import UserStatusEnum


class User(models.Model):
    account = models.CharField(
        max_length=32,
        # unique=True
    )
    password = models.CharField(
        max_length=32,
        db_index=True
    )
    name = models.CharField(
        max_length=255,
        db_index=True
    )
    status = models.CharField(
        max_length=64,
        db_index=True,
        choices=UserStatusEnum.choices,
        default=UserStatusEnum.ACTIVE.value
    )
    email = models.EmailField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.account}"

    class Meta:
        verbose_name = _("AdminUser")
        verbose_name_plural = _("AdminUsers")

    def save(self, *args, **kwargs):
        if self.password is None:
            self.password = get_random_string(length=12, special=True)
        super().save(*args, **kwargs)


class UserSession(models.Model):
    user = models.ForeignKey(
        "governance.User",
        on_delete=models.CASCADE,
        db_index=True
    )
    session_id = models.CharField(
        max_length=36,  # UUID (8-4-4-4-12)
        db_index=True,
        unique=True
    )
    expire_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.session_id}({self.user})"

    class Meta:
        verbose_name = _("Session")
        verbose_name_plural = _("Sessions")

    def save(self, *args, **kwargs):
        if not self.session_id:
            self.session_id = str(uuid.uuid4())
        if not self.expire_at:
            self.expire_at = (Timestamp() + env.get("ADMIN_USER_SESSION_EXPIRE_TIME", 0)).datetime
        super().save(*args, **kwargs)


class UserHistory(models.Model):
    user = models.ForeignKey(
        "governance.User",
        on_delete=models.RESTRICT,
        db_index=True
    )
