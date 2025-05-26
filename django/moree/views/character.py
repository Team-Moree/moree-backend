from django.contrib.auth.models import AnonymousUser
from rest_framework import filters, mixins
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema

from core.pagenation import BasePagination
from core.views import BaseGenericAPIView
from core.enums import StatusEnum

from moree.permissions import UserPermission
from moree.models import (
    Character
)
from moree.filters import (
    CharacterFilter
)
from moree.serializers import (
    CharacterSerializer
)


class CharacterView(
    mixins.ListModelMixin,
    BaseGenericAPIView
):
    serializer_class = CharacterSerializer
    pagination_class = BasePagination

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = CharacterFilter

    def get_queryset(self):
        queryset = Character.objects.filter(
            status=StatusEnum.ACTIVE.value,
        ).order_by("-id")
        return queryset

    def get_permissions(self):
        return super().get_permissions()

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CharacterDetailView(
    mixins.RetrieveModelMixin,
    BaseGenericAPIView
):
    serializer_class = CharacterSerializer

    def get_queryset(self):
        queryset = Character.objects.filter(
            status=StatusEnum.ACTIVE.value,
        ).order_by("-id")
        return queryset

    def get_permissions(self):
        return super().get_permissions()

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
