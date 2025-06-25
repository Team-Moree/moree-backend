from typing import Tuple

import jwt

from rest_framework import serializers

from core.environment import env
from lib.request import ExternalRequest
from lib.timestamp import Timestamp
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
from moree.enums import (
    UserGenderEnum,
    UserProviderEnum
)
from moree.exceptions import (
    UserDoesNotExistError,
    UserTermAgreementRequiredError,
    ProviderTokenExpiredError,
    InvalidProviderTokenError,
    UnknownProviderTokenError
)


class UserSerializer(serializers.ModelSerializer):
    gender = serializers.ChoiceField(choices=UserGenderEnum.choices)

    class Meta:
        model = User
        read_only_fields = ("email",)


class UserAccessTokenSerializer(serializers.ModelSerializer):
    refresh_token = serializers.CharField(write_only=True)
    class Meta:
        model = UserAccessToken
        read_only_fields = ("user",)
        exclude = (
            "id",
            "user_refresh_token",
            "device_id",
            "expire_at",
            "created_at",
            "updated_at",
            "deleted_at"
        )


class UserRefreshTokenSerializer(serializers.ModelSerializer):
    device_id = serializers.CharField(write_only=True)
    provider = serializers.ChoiceField(choices=UserProviderEnum.choices)
    provider_token = serializers.CharField(write_only=True)

    class Meta:
        model = UserRefreshToken
        read_only_fields = ("user",)
        exclude = (
            "id",
            "expire_at",
            "created_at",
            "updated_at",
            "deleted_at"
        )

    @staticmethod
    def verify_provider_token(provider: UserProviderEnum, provider_token: str) -> Tuple[str, str]:
        er = ExternalRequest()

        match provider:
            case UserProviderEnum.APPLE.value:
                jwt_client = jwt.PyJWKClient(env.get("APPLE_PUBLIC_KEYS_URL"))

                try:
                    signing_key = jwt_client.get_signing_key_from_jwt(provider_token)
                    context = jwt.decode(
                        provider_token,
                        signing_key.key,
                        audience=env.get("APPLE_CLIENT_ID"),
                        algorithms=["RS256"],
                    )
                    provider_user_id = context.get("sub", "")
                    email = context.get("email", "")
                except jwt.ExpiredSignatureError:
                    raise ProviderTokenExpiredError()
                except jwt.InvalidTokenError:
                    raise InvalidProviderTokenError()
                except Exception:
                    raise UnknownProviderTokenError()
            case UserProviderEnum.GOOGLE.value:
                response = er.get(
                    env.get("GOOGLE_OAUTH_URL"),
                    params={"id_token": provider_token}
                )
                if response.status_code != 200:
                    raise InvalidProviderTokenError()

                context = response.json()
                provider_user_id = context.get("sub", "")
                email = context.get("email", "")

        return provider_user_id, email

    def create(self, validated_data):
        device_id = validated_data.pop("device_id")
        provider = validated_data.get("provider")
        provider_token = validated_data.pop("provider_token")

        provider_user_id, email = UserRefreshTokenSerializer.verify_provider_token(
            provider, 
            provider_token
        )

        user = User.objects.filter(
            email=email,
            provider=provider,
            provider_user_id=provider_user_id,
            device_id=device_id
        ).first()

        if user is None:
            raise UserDoesNotExistError()
        
        # 유저 이용약관 동의 여부?
        if user.is_agreed_terms is not True:
            raise UserTermAgreementRequiredError()
        

        validated_data["user"] = user
        validated_data["provider_user_id"] = provider_user_id
        validated_data["expire_at"] = (Timestamp() + int(env.get("MOREE_USER_SESSION_EXPIRE_TIME", 3600))).datetime

        return super().create(validated_data)


# class UserLogSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserLog


class UserCharacterInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCharacterInventory


class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReview


class UserReviewReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReviewReport


class UserStoreBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStoreBookmark


class UserStoreCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStoreCategory


class UserStoreStampSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStoreStamp


class UserTermAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTermAgreement
