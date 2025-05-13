from datetime import datetime
from django_filters import rest_framework
from rest_framework.exceptions import ValidationError


class EpochTimeFilter(rest_framework.Filter):
    def filter(self, qs, value):
        if value is None:
            return qs
        try:
            timestamp = float(value)
            dt_value = datetime.fromtimestamp(timestamp)
        except (ValueError, OSError):
            raise ValidationError(f"Invalid epoch time: {value}")
        return super().filter(qs, dt_value)


class BaseFilter(rest_framework.FilterSet):
    created_at = EpochTimeFilter(field_name="created_at", lookup_expr="exact")
    created_at_gt = EpochTimeFilter(field_name="created_at", lookup_expr="gt")
    created_at_gte = EpochTimeFilter(field_name="created_at", lookup_expr="gte")
    created_at_lt = EpochTimeFilter(field_name="created_at", lookup_expr="lt")
    created_at_lte = EpochTimeFilter(field_name="created_at", lookup_expr="lte")

    updated_at = EpochTimeFilter(field_name="updated_at", lookup_expr="exact")
    updated_at_gt = EpochTimeFilter(field_name="updated_at", lookup_expr="gt")
    updated_at_gte = EpochTimeFilter(field_name="updated_at", lookup_expr="gte")
    updated_at_lt = EpochTimeFilter(field_name="updated_at", lookup_expr="lt")
    updated_at_lte = EpochTimeFilter(field_name="updated_at", lookup_expr="lte")

    class Meta:
        fields = ["created_at", "updated_at"]
