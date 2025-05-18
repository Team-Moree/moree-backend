from django.db.models import TextChoices


class TermAgreementTypeEnum(TextChoices):
    REQUIRED = "REQUIRED", "Required"
    OPTIONAL = "OPTIONAL", "Optional"
