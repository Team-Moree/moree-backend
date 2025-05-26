from django.contrib.auth.models import AnonymousUser
from rest_framework import filters, mixins
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema

from core.pagenation import BasePagination
from core.views import BaseGenericAPIView
from core.enums import StatusEnum

from moree.permissions import UserPermission
from moree.models import (
    Store,
    StoreCategory,
    StoreCharacterPool
)
from moree.filters import (
    StoreFilter,
    StoreCategoryFilter,
    StoreCharacterPoolFilter
)
from moree.serializers import (
    StoreSerializer,
    StoreCategorySerializer,
    StoreCharacterPoolSerializer
)


class StoreView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    BaseGenericAPIView
):
    serializer_class = StoreSerializer
    pagination_class = BasePagination

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = StoreFilter

    def get_queryset(self):
        queryset = Store.objects.filter(
            status=StatusEnum.ACTIVE.value,
        ).order_by("-id")
        return queryset

    def get_permissions(self):
        if self.request.method in ("POST",):
            return [UserPermission()]
        return super().get_permissions()

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema()
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StoreDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    BaseGenericAPIView
):
    serializer_class = StoreSerializer

    def get_queryset(self):
        queryset = Store.objects.filter(
            status=StatusEnum.ACTIVE.value,
        ).order_by("-id")
        return queryset

    def get_permissions(self):
        if self.request.method in ("PUT", "PATCH", "DELETE"):
            return [UserPermission()]
        return super().get_permissions()

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema()
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema()
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema()
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StoreCategoryView(
    mixins.ListModelMixin,
    BaseGenericAPIView
):
    serializer_class = StoreCategorySerializer
    pagination_class = BasePagination

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = StoreCategoryFilter

    def get_queryset(self):
        queryset = StoreCategory.objects.filter(
            status=StatusEnum.ACTIVE.value,
        ).order_by("-id")
        return queryset

    def get_permissions(self):
        if self.request.method in ("POST",):
            return [UserPermission()]
        return super().get_permissions()

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class StoreCategoryDetailView(
    mixins.RetrieveModelMixin,
    BaseGenericAPIView
):
    serializer_class = StoreCategorySerializer

    def get_queryset(self):
        queryset = StoreCategory.objects.filter(
            status=StatusEnum.ACTIVE.value,
        ).order_by("-id")
        return queryset

    def get_permissions(self):
        return super().get_permissions()

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class StoreCharacterPoolView(
    mixins.ListModelMixin,
    BaseGenericAPIView
):
    serializer_class = StoreCharacterPoolSerializer
    pagination_class = BasePagination

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = StoreCharacterPoolFilter

    def get_queryset(self):
        queryset = StoreCharacterPool.objects.filter(
            status=StatusEnum.ACTIVE.value,
        ).order_by("-id")
        return queryset

    def get_permissions(self):
        if self.request.method in ("POST",):
            return [UserPermission()]
        return super().get_permissions()

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class StoreCharacterPoolDetailView(
    mixins.RetrieveModelMixin,
    BaseGenericAPIView
):
    serializer_class = StoreCharacterPoolSerializer

    def get_queryset(self):
        queryset = StoreCharacterPool.objects.filter(
            status=StatusEnum.ACTIVE.value,
        ).order_by("-id")
        return queryset

    def get_permissions(self):
        return super().get_permissions()

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
