import logging

from django.utils.translation import gettext_lazy as _

from lib.request import Request

from core.exceptions import ExternalRequestError


class ExternalRequest(Request):
    def __init__(self, *args, **kwargs):
        logger = logging.getLogger("external")
        super().__init__(*args, logger=logger, **kwargs)

    def request(self, *args, **kwargs):
        try:
            return super().request(*args, **kwargs)
        except TypeError:
            raise ExternalRequestError(_("외부 API 호출용 Body 파싱 실패"))
        except Exception:
            raise ExternalRequestError()


__all__ = ("ExternalRequest",)
