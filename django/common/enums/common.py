from django.db.models import TextChoices


class UploaderTypeEnum(TextChoices):
    ADMIN = "ADMIN", "Admin"
    USER = "USER", "User"
