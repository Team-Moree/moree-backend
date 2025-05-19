from django_filters import rest_framework

from common.models import (
    StoredFile,
    StoredFilesGroup
)

from core.filters import BaseFilter


class StoredFileFilter(BaseFilter):
    name = rest_framework.CharFilter(field_name="name", lookup_expr="iexact")
    name_contains = rest_framework.CharFilter(field_name="name", lookup_expr="icontains")

    ext = rest_framework.CharFilter(field_name="ext", lookup_expr="iexact")
    ext_contains = rest_framework.CharFilter(field_name="ext", lookup_expr="icontains")

    class Meta:
        model = StoredFile
        fields = "__all__"


class StoredFilesGroupFilter(BaseFilter):
    name = rest_framework.CharFilter(field_name="name", lookup_expr="iexact")
    name_contains = rest_framework.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = StoredFilesGroup
        fields = "__all__"
