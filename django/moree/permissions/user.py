from rest_framework.permissions import BasePermission
from moree.models import User


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        # TODO: 추후 provider login-in 구현
        request.user = User.objects.get(id=1)
        return True

        authorization_header = request.headers.get("Authorization")

        if authorization_header is None:
            return False

        if not authorization_header.startswith("Bearer "):
            return False

        user_access_token = authorization_header[7:]

        return False
