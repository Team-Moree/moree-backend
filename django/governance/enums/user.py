from django.db.models import TextChoices


class UserStatusEnum(TextChoices):
    ACTIVE = "ACTIVE", "Active"
    WITHDRAWN = "WITHDRAWN", "Withdrawn"
