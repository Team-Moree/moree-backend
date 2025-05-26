from django.contrib.auth.models import AnonymousUser
from rest_framework import filters, mixins
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema

from core.pagenation import BasePagination
from core.views import BaseGenericAPIView
from core.enums import StatusEnum

from moree.permissions import UserPermission
from moree.models import (
    Term,
    TermCategory
)
from moree.filters import (
    TermFilter,
    TermCategoryFilter
)
from moree.serializers import (
    TermSerializer,
    TermCategorySerializer
)


class TermView(
    mixins.ListModelMixin,
    BaseGenericAPIView
):
    serializer_class = TermSerializer
    pagination_class = BasePagination

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = TermFilter

    def get_queryset(self):
        queryset = Term.objects.filter(
            status=StatusEnum.ACTIVE.value,
        ).order_by("-id")
        return queryset

    def get_permissions(self):
        return super().get_permissions()

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TermDetailView(
    mixins.RetrieveModelMixin,
    BaseGenericAPIView
):
    serializer_class = TermSerializer

    def get_queryset(self):
        queryset = Term.objects.filter(
            status=StatusEnum.ACTIVE.value,
        ).order_by("-id")
        return queryset

    def get_permissions(self):
        return super().get_permissions()

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class TermCategoryView(
    mixins.ListModelMixin,
    BaseGenericAPIView
):
    serializer_class = TermCategorySerializer
    pagination_class = BasePagination

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = TermCategoryFilter

    def get_queryset(self):
        queryset = TermCategory.objects.filter(
            status=StatusEnum.ACTIVE.value,
        ).order_by("-id")
        return queryset

    def get_permissions(self):
        return super().get_permissions()

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TermCategoryDetailView(
    mixins.RetrieveModelMixin,
    BaseGenericAPIView
):
    serializer_class = TermCategorySerializer

    def get_queryset(self):
        queryset = TermCategory.objects.filter(
            status=StatusEnum.ACTIVE.value,
        ).order_by("-id")
        return queryset

    def get_permissions(self):
        return super().get_permissions()

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
