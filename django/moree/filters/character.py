from django_filters import rest_framework

from core.filters import BaseFilter
from moree.models import (
    Character
)


class CharacterFilter(BaseFilter):
    name = rest_framework.CharFilter(field_name="name", lookup_expr="iexact")
    name_contains = rest_framework.CharFilter(field_name="name", lookup_expr="icontains")

    status = rest_framework.CharFilter(field_name="status", lookup_expr="iexact")

    class Meta:
        model = Character
        fields = "__all__"
