from django_filters import rest_framework

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

from core.filters import BaseFilter


class UserFilter(BaseFilter):
    name = rest_framework.CharFilter(field_name="name", lookup_expr="iexact")
    name_contains = rest_framework.CharFilter(field_name="name", lookup_expr="icontains")

    email = rest_framework.CharFilter(field_name="email", lookup_expr="iexact")
    email_contains = rest_framework.CharFilter(field_name="email", lookup_expr="icontains")

    gender = rest_framework.CharFilter(field_name="gender", lookup_expr="iexact")

    status = rest_framework.CharFilter(field_name="status", lookup_expr="iexact")

    birthday = rest_framework.DateFilter(field_name="birthday", lookup_expr="exact")
    birthday_gt = rest_framework.DateFilter(field_name="birthday", lookup_expr="gt")
    birthday_gte = rest_framework.DateFilter(field_name="birthday", lookup_expr="gte")
    birthday_lt = rest_framework.DateFilter(field_name="birthday", lookup_expr="lt")
    birthday_lte = rest_framework.DateFilter(field_name="birthday", lookup_expr="lte")

    class Meta:
        model = User
        fields = [
            "name",
            "email",
            "gender",
            "status",
            "birthday"
        ]


class UserAccessTokenFilter(BaseFilter):
    class Meta:
        model = UserAccessToken
        fields = "__all__"


class UserRefreshTokenFilter(BaseFilter):
    class Meta:
        model = UserRefreshToken
        fields = "__all__"

# class UserLogFilter(BaseFilter):
#     class Meta:
#         model = UserLog
#         fields = "__all__"


class UserCharacterInventoryFilter(BaseFilter):
    class Meta:
        model = UserCharacterInventory
        fields = "__all__"


class UserReviewFilter(BaseFilter):
    class Meta:
        model = UserReview
        fields = "__all__"


class UserReviewReportFilter(BaseFilter):
    class Meta:
        model = UserReviewReport
        fields = "__all__"


class UserStoreBookmarkFilter(BaseFilter):
    class Meta:
        model = UserStoreBookmark
        fields = "__all__"


class UserStoreCategoryFilter(BaseFilter):
    class Meta:
        model = UserStoreCategory
        fields = "__all__"


class UserStoreStampFilter(BaseFilter):
    class Meta:
        model = UserStoreStamp
        fields = "__all__"


class UserTermAgreementFilter(BaseFilter):
    class Meta:
        model = UserTermAgreement
        fields = "__all__"
