from django_filters import rest_framework

from core.filters import BaseFilter
from moree.models import (
    Term,
    TermCategory
)


class TermFilter(BaseFilter):
    agreement_type = rest_framework.CharFilter(field_name="agreement_type", lookup_expr="iexact")

    name = rest_framework.CharFilter(field_name="name", lookup_expr="iexact")
    name_contains = rest_framework.CharFilter(field_name="name", lookup_expr="icontains")

    priority = rest_framework.NumberFilter(field_name="priority", lookup_expr="exact")

    status = rest_framework.CharFilter(field_name="status", lookup_expr="iexact")

    class Meta:
        model = Term
        fields = "__all__"


class TermCategoryFilter(BaseFilter):
    name = rest_framework.CharFilter(field_name="name", lookup_expr="iexact")
    name_contains = rest_framework.CharFilter(field_name="name", lookup_expr="icontains")

    status = rest_framework.CharFilter(field_name="status", lookup_expr="iexact")

    class Meta:
        model = TermCategory
        fields = "__all__"
