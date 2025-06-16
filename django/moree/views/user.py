from django.contrib.auth.models import AnonymousUser
from rest_framework import filters, mixins
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema

from core.pagenation import BasePagination
from core.views import BaseGenericAPIView

from moree.models import (
    User,
    UserAccessToken,
    UserRefreshToken,
    UserLog,
    UserCharacterInventory,
    UserReview,
    UserReviewReport,
    UserStoreBookmark,
    UserStoreCategory,
    UserStoreStamp,
    UserTermAgreement,
)
from moree.filters import (
    UserFilter,
    UserAccessTokenFilter,
    UserRefreshTokenFilter,
    # UserLogFilter,
    UserCharacterInventoryFilter,
    UserReviewFilter,
    UserReviewReportFilter,
    UserStoreBookmarkFilter,
    UserStoreCategoryFilter,
    UserStoreStampFilter,
    UserTermAgreementFilter,
)
from moree.enums import UserStatusEnum
from moree.permissions import UserPermission
from moree.serializers import (
    UserSerializer,
    UserAccessTokenSerializer,
    UserRefreshTokenSerializer,
    # UserLogSerializer,
    UserCharacterInventorySerializer,
    UserReviewSerializer,
    UserReviewReportSerializer,
    UserStoreBookmarkSerializer,
    UserStoreCategorySerializer,
    UserStoreStampSerializer,
    UserTermAgreementSerializer,
)


class UserView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
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
                status=UserStatusEnum.ACTIVE.value,
            ).order_by("-id")
        elif isinstance(self.request.user, AnonymousUser):
            queryset = User.objects.none()
        return queryset

    def get_permissions(self):
        if self.request.method in ("GET",):
            return [UserPermission()]
        return super().get_permissions()

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema()
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    BaseGenericAPIView
):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = None
        if isinstance(self.request.user, User):
            queryset = User.objects.filter(
                id=self.request.user.id,
                status=UserStatusEnum.ACTIVE.value,
            ).order_by("-id")
        elif isinstance(self.request.user, AnonymousUser):
            queryset = User.objects.none()
        return queryset

    def get_permissions(self):
        if self.request.method in ("GET", "PUT", "PATCH", "DELETE"):
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


class UserAccessTokenView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    BaseGenericAPIView
):
    serializer_class = UserAccessTokenSerializer
    pagination_class = BasePagination

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = UserAccessTokenFilter

    def get_queryset(self):
        queryset = None
        if isinstance(self.request.user, User):
            queryset = UserAccessToken.objects.filter(
                user=self.request.user,
            ).order_by("-id")
        elif isinstance(self.request.user, AnonymousUser):
            queryset = UserAccessToken.objects.none()
        return queryset

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema()
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserAccessTokenDetailView(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    BaseGenericAPIView
):
    serializer_class = UserAccessTokenSerializer

    def get_queryset(self):
        queryset = None
        if isinstance(self.request.user, User):
            queryset = UserAccessToken.objects.filter(
                user=self.request.user,
            ).order_by("-id")
        elif isinstance(self.request.user, AnonymousUser):
            queryset = UserAccessToken.objects.none()
        return queryset

    def get_permissions(self):
        if self.request.method in ("DELETE",):
            return [UserPermission()]
        return super().get_permissions()

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema()
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserRefreshTokenView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    BaseGenericAPIView
):
    serializer_class = UserRefreshTokenSerializer
    pagination_class = BasePagination

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = UserRefreshTokenFilter

    def get_queryset(self):
        queryset = None
        if isinstance(self.request.user, User):
            queryset = UserRefreshToken.objects.filter(
                user=self.request.user,
            ).order_by("-id")
        elif isinstance(self.request.user, AnonymousUser):
            queryset = UserRefreshToken.objects.none()
        return queryset

    def get_permissions(self):
        return super().get_permissions()

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema()
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserRefreshTokenDetailView(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    BaseGenericAPIView
):
    serializer_class = UserRefreshTokenSerializer

    def get_queryset(self):
        queryset = None
        if isinstance(self.request.user, User):
            queryset = UserRefreshToken.objects.filter(
                user=self.request.user,
            ).order_by("-id")
        elif isinstance(self.request.user, AnonymousUser):
            queryset = UserRefreshToken.objects.none()
        return queryset

    def get_permissions(self):
        if self.request.method in ("DELETE",):
            return [UserPermission()]
        return super(UserRefreshTokenDetailView, self).get_permissions()

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema()
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserCharacterInventoryView(
    mixins.ListModelMixin,
    BaseGenericAPIView
):
    serializer_class = UserCharacterInventorySerializer
    pagination_class = BasePagination

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = UserCharacterInventoryFilter

    def get_queryset(self):
        queryset = None
        if isinstance(self.request.user, User):
            queryset = UserCharacterInventory.objects.filter(
                user=self.request.user,
                status=UserStatusEnum.ACTIVE.value,
            ).order_by("-id")
        elif isinstance(self.request.user, AnonymousUser):
            queryset = UserCharacterInventory.objects.none()
        return queryset

    def get_permissions(self):
        if self.request.method in ("GET",):
            return [UserPermission()]
        return super().get_permissions()

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserCharacterInventoryDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    BaseGenericAPIView
):
    serializer_class = UserCharacterInventorySerializer

    def get_queryset(self):
        queryset = None
        if isinstance(self.request.user, User):
            queryset = UserCharacterInventory.objects.filter(
                user=self.request.user,
                status=UserStatusEnum.ACTIVE.value,
            ).order_by("-id")
        elif isinstance(self.request.user, AnonymousUser):
            queryset = UserCharacterInventory.objects.none()
        return queryset

    def get_permissions(self):
        if self.request.method in ("GET", "PUT", "PATCH"):
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


class UserReviewView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    BaseGenericAPIView
):
    serializer_class = UserReviewSerializer
    pagination_class = BasePagination

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = UserReviewFilter

    def get_queryset(self):
        queryset = None
        if isinstance(self.request.user, User):
            queryset = UserReview.objects.filter(
                status=UserStatusEnum.ACTIVE.value,
            ).order_by("-id")
        elif isinstance(self.request.user, AnonymousUser):
            queryset = UserReview.objects.none()
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


class UserReviewDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    BaseGenericAPIView
):
    serializer_class = UserReviewSerializer

    def get_queryset(self):
        queryset = None
        if isinstance(self.request.user, User):
            queryset = UserReview.objects.filter(
                status=UserStatusEnum.ACTIVE.value,
            ).order_by("-id")
        elif isinstance(self.request.user, AnonymousUser):
            queryset = UserReview.objects.none()
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


class UserReviewReportView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    BaseGenericAPIView
):
    serializer_class = UserReviewReportSerializer
    pagination_class = BasePagination

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = UserReviewReportFilter

    def get_queryset(self):
        queryset = None
        if isinstance(self.request.user, User):
            queryset = UserReviewReport.objects.filter(
                status=UserStatusEnum.ACTIVE.value,
            ).order_by("-id")
        elif isinstance(self.request.user, AnonymousUser):
            queryset = UserReviewReport.objects.none()
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


class UserReviewReportDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    BaseGenericAPIView
):
    serializer_class = UserReviewReportSerializer

    def get_queryset(self):
        queryset = None
        if isinstance(self.request.user, User):
            queryset = UserReviewReport.objects.filter(
                status=UserStatusEnum.ACTIVE.value,
            ).order_by("-id")
        elif isinstance(self.request.user, AnonymousUser):
            queryset = UserReviewReport.objects.none()
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


class UserStoreBookmarkView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    BaseGenericAPIView
):
    serializer_class = UserStoreBookmarkSerializer
    pagination_class = BasePagination

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = UserStoreBookmarkFilter

    def get_queryset(self):
        queryset = None
        if isinstance(self.request.user, User):
            # TODO: 북마크 열람 권한에 따라 쿼리가 달라져야함.
            queryset = UserStoreBookmark.objects.filter(
                status=UserStatusEnum.ACTIVE.value,
            ).order_by("-id")
        elif isinstance(self.request.user, AnonymousUser):
            queryset = UserStoreBookmark.objects.none()
        return queryset

    def get_permissions(self):
        if self.request.method in ("GET", "POST"):
            return [UserPermission()]
        return super().get_permissions()

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema()
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserStoreBookmarkDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    BaseGenericAPIView
):
    serializer_class = UserStoreBookmarkSerializer

    def get_queryset(self):
        queryset = None
        if isinstance(self.request.user, User):
            queryset = UserStoreBookmark.objects.filter(
                status=UserStatusEnum.ACTIVE.value,
            ).order_by("-id")
        elif isinstance(self.request.user, AnonymousUser):
            queryset = UserStoreBookmark.objects.none()
        return queryset

    def get_permissions(self):
        if self.request.method in ("GET", "PUT", "PATCH", "DELETE"):
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


class UserStoreCategoryView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    BaseGenericAPIView
):
    serializer_class = UserStoreCategorySerializer
    pagination_class = BasePagination

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = UserStoreCategoryFilter


    def get_queryset(self):
        queryset = None
        if isinstance(self.request.user, User):
            queryset = UserStoreCategory.objects.filter(
                user=self.request.user,
                status=UserStatusEnum.ACTIVE.value,
            ).order_by("-id")
        elif isinstance(self.request.user, AnonymousUser):
            queryset = UserStoreCategory.objects.none()
        return queryset

    def get_permissions(self):
        if self.request.method in ("GET", "POST"):
            return [UserPermission()]
        return super().get_permissions()

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema()
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserStoreCategoryDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    BaseGenericAPIView
):
    serializer_class = UserStoreCategorySerializer

    def get_queryset(self):
        queryset = None
        if isinstance(self.request.user, User):
            queryset = UserStoreCategory.objects.filter(
                user=self.request.user,
                status=UserStatusEnum.ACTIVE.value,
            ).order_by("-id")
        elif isinstance(self.request.user, AnonymousUser):
            queryset = UserStoreCategory.objects.none()
        return queryset

    def get_permissions(self):
        if self.request.method in ("GET", "PUT", "PATCH", "DELETE"):
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


class UserStoreStampView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    BaseGenericAPIView
):
    serializer_class = UserStoreStampSerializer
    pagination_class = BasePagination

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = UserStoreStampFilter

    def get_queryset(self):
        queryset = None
        if isinstance(self.request.user, User):
            queryset = UserStoreStamp.objects.filter(
                user=self.request.user,
                status=UserStatusEnum.ACTIVE.value,
            ).order_by("-id")
        elif isinstance(self.request.user, AnonymousUser):
            queryset = UserStoreStamp.objects.none()
        return queryset

    def get_permissions(self):
        if self.request.method in ("GET", "POST"):
            return [UserPermission()]
        return super().get_permissions()

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema()
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserStoreStampDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    BaseGenericAPIView
):
    serializer_class = UserStoreStampSerializer

    def get_queryset(self):
        queryset = None
        if isinstance(self.request.user, User):
            queryset = UserStoreStamp.objects.filter(
                user=self.request.user,
                status=UserStatusEnum.ACTIVE.value,
            ).order_by("-id")
        elif isinstance(self.request.user, AnonymousUser):
            queryset = UserStoreStamp.objects.none()
        return queryset

    def get_permissions(self):
        if self.request.method in ("GET", "PUT", "PATCH", "DELETE"):
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


class UserTermAgreementView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    BaseGenericAPIView
):
    serializer_class = UserTermAgreementSerializer
    pagination_class = BasePagination

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = UserTermAgreementFilter

    def get_queryset(self):
        queryset = None
        # TODO: 같은 카테고리의 동의 내역에 대해서는 마지막 1개만 노출되도록 변경해야함.
        if isinstance(self.request.user, User):
            queryset = UserTermAgreement.objects.filter(
                user=self.request.user,
                status=UserStatusEnum.ACTIVE.value,
            ).order_by("-id")
        elif isinstance(self.request.user, AnonymousUser):
            queryset = UserTermAgreement.objects.none()
        return queryset

    def get_permissions(self):
        if self.request.method in ("GET", "POST"):
            return [UserPermission()]
        return super().get_permissions()

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema()
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserTermAgreementDetailView(
    mixins.RetrieveModelMixin,
    BaseGenericAPIView
):
    serializer_class = UserTermAgreementSerializer

    def get_queryset(self):
        queryset = None
        if isinstance(self.request.user, User):
            queryset = UserTermAgreement.objects.filter(
                user=self.request.user,
                status=UserStatusEnum.ACTIVE.value,
            ).order_by("-id")
        elif isinstance(self.request.user, AnonymousUser):
            queryset = UserTermAgreement.objects.none()
        return queryset

    def get_permissions(self):
        if self.request.method in ("GET",):
            return [UserPermission()]
        return super().get_permissions()

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
