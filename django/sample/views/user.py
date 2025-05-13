from django.contrib.auth.models import AnonymousUser
from rest_framework import filters, mixins
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema

from core.pagenation import BasePagination
from core.views import BaseGenericAPIView

from sample.models import User
from sample.filters import UserFilter
from sample.enums import UserStatusEnum
from sample.permissions import UserPermission
from sample.serializers import UserSerializer

from governance.models import User as AdminUser
from governance.permissions import UserPermission as AdminUserPermission


class UserView(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    BaseGenericAPIView
):
    serializer_class = UserSerializer
    pagination_class = BasePagination

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = UserFilter

    def get_queryset(self):
        queryset = None
        if isinstance(self.request.user, User):
            queryset = User.objects.filter(
                id=self.request.user.id,
                status=UserStatusEnum.ACTIVE,
            )
        elif isinstance(self.request.user, AdminUser):
            queryset = User.objects.all()
        elif isinstance(self.request.user, AnonymousUser):
            # queryset = User.objects.none()
            queryset = User.objects.all()
        return queryset

    def get_permissions(self):
        if self.request.method in ("GET", "DELETE"):
            return [UserPermission(), AdminUserPermission()]
        elif self.request.method in ("PUT", "PATCH"):
            return [UserPermission()]
        return super().get_permissions()

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema()
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    @swagger_auto_schema()
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema()
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema()
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    BaseGenericAPIView
):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    def get_permissions(self):
        if self.request.method in ("GET", "PUT", "PATCH", "DELETE"):
            return [AdminUserPermission()]
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
