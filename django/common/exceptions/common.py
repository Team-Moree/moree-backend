from rest_framework.exceptions import APIException

from django.utils.translation import gettext_lazy as _


class ExternalRequestError(APIException):
    default_detail = {
        "status_code": 10000,
        "message": _("외부 API 호출 오류")
    }
