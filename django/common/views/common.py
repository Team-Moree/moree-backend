from django.contrib.auth.models import AnonymousUser
from rest_framework import filters, mixins
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema

from core.pagenation import BasePagination
from core.views import BaseGenericAPIView
from core.enums import StatusEnum

from moree.permissions import UserPermission
from moree.models import User

from common.models import (
    StoredFile,
    StoredFilesGroup
)
from common.enums import UploaderTypeEnum
from common.serializers import (
    StoredFileSerializer,
    StoredFilesGroupSerializer
)
from common.filters import (
    StoredFileFilter,
    StoredFilesGroupFilter
)


class StoredFileView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    BaseGenericAPIView
):
    serializer_class = StoredFileSerializer
    pagination_class = BasePagination

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = StoredFileFilter

    def get_queryset(self):
        queryset = None
        # TODO: 권한 별로 볼 수 있는 영역을 나눠야함

        # if isinstance(self.request.user, User):
        #     queryset = StoredFile.objects.filter(
        #         uploader_type=UploaderTypeEnum.USER.value,
        #         uploader_id=self.request.user.id,
        #         status=StatusEnum.ACTIVE.value,
        #     ).order_by("-id")
        # elif isinstance(self.request.user, AnonymousUser):
        #     # queryset = StoredFile.objects.none()
        #     queryset = StoredFile.objects.all().order_by("-id")
        queryset = StoredFile.objects.filter(
            status=StatusEnum.ACTIVE.value
        ).order_by("-id")
        return queryset

    def get_permissions(self):
        if self.request.method in ("POST", "DELETE"):
            return [UserPermission()]
        return super().get_permissions()

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema()
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StoredFileDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    BaseGenericAPIView
):
    serializer_class = StoredFileSerializer

    def get_queryset(self):
        queryset = None
        if self.request.method in ("GET"):
            queryset = User.objects.filter(
                status=StatusEnum.ACTIVE.value
            ).order_by("-id")
        elif self.request.method in ("PUT", "PATCH", "DELETE"):
            queryset = StoredFile.objects.filter(
                uploader_type=UploaderTypeEnum.USER.value,
                uploader_id=self.request.user.id,
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


class StoredFilesGroupView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    BaseGenericAPIView
):
    serializer_class = StoredFilesGroupSerializer
    pagination_class = BasePagination

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = StoredFilesGroupFilter

    def get_queryset(self):
        queryset = StoredFilesGroup.objects.filter(
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


class StoredFilesGroupDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    BaseGenericAPIView
):
    serializer_class = StoredFilesGroupSerializer

    def get_queryset(self):
        queryset = StoredFilesGroup.objects.filter(
            status=StatusEnum.ACTIVE.value
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
