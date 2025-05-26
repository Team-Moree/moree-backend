from django_filters import rest_framework

from core.filters import BaseFilter, EpochTimeFilter
from moree.models import (
    Store,
    StoreCategory,
    StoreCharacterPool
)


class StoreFilter(BaseFilter):
    title = rest_framework.CharFilter(field_name="title", lookup_expr="iexact")
    title_contains = rest_framework.CharFilter(field_name="title", lookup_expr="icontains")

    address = rest_framework.CharFilter(field_name="address", lookup_expr="iexact")
    address_contains = rest_framework.CharFilter(field_name="address", lookup_expr="icontains")

    business_day_mask = rest_framework.NumberFilter(method="business_day_mask")

    latitude = rest_framework.NumberFilter(field_name="latitude", lookup_expr="exact")
    latitude_gt = rest_framework.NumberFilter(field_name="latitude", lookup_expr="gt")
    latitude_gte = rest_framework.NumberFilter(field_name="latitude", lookup_expr="gte")
    latitude_lt = rest_framework.NumberFilter(field_name="latitude", lookup_expr="lt")
    latitude_lte = rest_framework.NumberFilter(field_name="latitude", lookup_expr="lte")

    longitude = rest_framework.NumberFilter(field_name="longitude", lookup_expr="exact")
    longitude_gt = rest_framework.NumberFilter(field_name="longitude", lookup_expr="gt")
    longitude_gte = rest_framework.NumberFilter(field_name="longitude", lookup_expr="gte")
    longitude_lt = rest_framework.NumberFilter(field_name="longitude", lookup_expr="lt")
    longitude_lte = rest_framework.NumberFilter(field_name="longitude", lookup_expr="lte")

    status = rest_framework.CharFilter(field_name="status", lookup_expr="iexact")

    start_date = rest_framework.DateFilter(field_name="start_date", lookup_expr="exact")
    start_date_gt = rest_framework.DateFilter(field_name="start_date", lookup_expr="gt")
    start_date_gte = rest_framework.DateFilter(field_name="start_date", lookup_expr="gte")
    start_date_lt = rest_framework.DateFilter(field_name="start_date", lookup_expr="lt")
    start_date_lte = rest_framework.DateFilter(field_name="start_date", lookup_expr="lte")

    end_date = rest_framework.DateFilter(field_name="end_date", lookup_expr="exact")
    end_date_gt = rest_framework.DateFilter(field_name="end_date", lookup_expr="gt")
    end_date_gte = rest_framework.DateFilter(field_name="end_date", lookup_expr="gte")
    end_date_lt = rest_framework.DateFilter(field_name="end_date", lookup_expr="lt")
    end_date_lte = rest_framework.DateFilter(field_name="end_date", lookup_expr="lte")

    opening_time = rest_framework.TimeFilter(field_name="opening_time", lookup_expr="exact")
    opening_time_gt = rest_framework.TimeFilter(field_name="opening_time", lookup_expr="gt")
    opening_time_gte = rest_framework.TimeFilter(field_name="opening_time", lookup_expr="gte")
    opening_time_lt = rest_framework.TimeFilter(field_name="opening_time", lookup_expr="lt")
    opening_time_lte = rest_framework.TimeFilter(field_name="opening_time", lookup_expr="lte")

    closing_time = rest_framework.TimeFilter(field_name="closing_time", lookup_expr="exact")
    closing_time_gt = rest_framework.TimeFilter(field_name="closing_time", lookup_expr="gt")
    closing_time_gte = rest_framework.TimeFilter(field_name="closing_time", lookup_expr="gte")
    closing_time_lt = rest_framework.TimeFilter(field_name="closing_time", lookup_expr="lt")
    closing_time_lte = rest_framework.TimeFilter(field_name="closing_time", lookup_expr="lte")

    pre_order_start_at = EpochTimeFilter(field_name="pre_order_start_at", lookup_expr="exact")
    pre_order_start_at_gt = EpochTimeFilter(field_name="pre_order_start_at", lookup_expr="gt")
    pre_order_start_at_gte = EpochTimeFilter(field_name="pre_order_start_at", lookup_expr="gte")
    pre_order_start_at_lt = EpochTimeFilter(field_name="pre_order_start_at", lookup_expr="lt")
    pre_order_start_at_lte = EpochTimeFilter(field_name="pre_order_start_at", lookup_expr="lte")

    def business_day_mask(self, queryset, name, value):
        return queryset.filter(business_day__bitand=value).exclude(business_day__bitand=value==0)

    class Meta:
        model = Store
        fields = "__all__"


class StoreCategoryFilter(BaseFilter):
    name = rest_framework.CharFilter(field_name="name", lookup_expr="iexact")
    name_contains = rest_framework.CharFilter(field_name="name", lookup_expr="icontains")

    priority = rest_framework.NumberFilter(field_name="priority", lookup_expr="exact")

    status = rest_framework.CharFilter(field_name="status", lookup_expr="iexact")

    class Meta:
        model = StoreCategory
        fields = "__all__"


class StoreCharacterPoolFilter(BaseFilter):
    weight = rest_framework.NumberFilter(field_name="weight", lookup_expr="exact")

    status = rest_framework.CharFilter(field_name="status", lookup_expr="iexact")

    class Meta:
        model = StoreCharacterPool
        fields = "__all__"
