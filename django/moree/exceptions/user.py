from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import (
    AuthenticationFailed,
    NotFound,
    PermissionDenied
)


class UserDoesNotExistError(NotFound):
    default_detail = {
        "status_code": 20000,
        "message": _("User does not exist"),
    }


class UserTermAgreementRequiredError(PermissionDenied):
    default_detail = {
        "status_code": 20001,
        "message": _("User term agreement required"),
    }


class UnknownProviderTokenError(AuthenticationFailed):
    default_detail = {
        "status_code": 20100,
        "message": _("Unknown provider token error"),
    }


class ProviderTokenExpiredError(AuthenticationFailed):
    default_detail = {
        "status_code": 20101,
        "message": _("Expired provider token"),
    }


class InvalidProviderTokenError(AuthenticationFailed):
    default_detail = {
        "status_code": 20102,
        "message": _("Invalid provider token error"),
    }


class ProviderEmailUserNotFoundError(NotFound):
    default_detail = {
        "status_code": 20103,
        "message": _(
            "Cannot find a user matching the email provided by the provider token"
        ),
    }


class UnknownAccessTokenError(AuthenticationFailed):
    default_detail = {
        "status_code": 20200,
        "message": _("Unknown access token error"),
    }


class AccessTokenExpiredError(AuthenticationFailed):
    default_detail = {
        "status_code": 20201,
        "message": _("Expired access token"),
    }


class InvalidAccessTokenError(AuthenticationFailed):
    default_detail = {
        "status_code": 20202,
        "message": _("Invalid access token error"),
    }


class InvalidAccessTokenDeviceId(AuthenticationFailed):
    default_detail = {
        "status_code": 20203,
        "message": _("Access token's device_id does not match"),
    }


class UnknownRefreshTokenError(AuthenticationFailed):
    default_detail = {
        "status_code": 20300,
        "message": _("Unknown refresh token error"),
    }


class RefreshTokenExpiredError(AuthenticationFailed):
    default_detail = {
        "status_code": 20301,
        "message": _("Expired refresh token"),
    }


class InvalidRefreshTokenError(AuthenticationFailed):
    default_detail = {
        "status_code": 20302,
        "message": _("Invalid refresh token error")
    }


class InvalidRefreshTokenDeviceId(AuthenticationFailed):
    default_detail = {
        "status_code": 20303,
        "message": _("Refresh token's device_id does not match"),
    }
