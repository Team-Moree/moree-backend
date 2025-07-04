from rest_framework import serializers

from moree.models import (
    User,
    UserAccessToken,
    UserRefreshToken,
    # UserLog,
    UserCharacterInventory,
    UserReview,
    UserReviewReport,
    UserStoreBookmark,
    UserStoreCategory,
    UserStoreStamp,
    UserTermAgreement
)
from moree.enums import UserGenderEnum


class UserSerializer(serializers.ModelSerializer):
    gender = serializers.ChoiceField(choices=UserGenderEnum.choices)

    class Meta:
        model = User
        read_only_fields = ("email",)
        exclude = ("status",)


class UserAccessTokenSerializer(serializers.ModelSerializer):
    refresh_token = serializers.CharField(write_only=True)
    class Meta:
        model = UserAccessToken
        read_only_fields = ("user",)
        exclude = (
            "user_refresh_token",
            "device_id",
            "expire_at",
            "created_at",
            "updated_at"
        )


class UserRefreshTokenSerializer(serializers.ModelSerializer):
    provider_token = serializers.CharField(write_only=True)
    class Meta:
        model = UserRefreshToken
        read_only_fields = ("user",)
        exclude = (
            "device_id",
            "provider",
            "provider_user_id",
            # "provider_token",
            "expire_at",
            "created_at",
            "updated_at"
        )


# class UserLogSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserLog
#         exclude = ("status",)


class UserCharacterInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCharacterInventory
        exclude = ("status",)


class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReview
        exclude = ("status",)


class UserReviewReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReviewReport
        exclude = ("status",)


class UserStoreBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStoreBookmark
        exclude = ("status",)


class UserStoreCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStoreCategory
        exclude = ("status",)


class UserStoreStampSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStoreStamp
        exclude = ("status",)


class UserTermAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTermAgreement
        exclude = ("status",)
