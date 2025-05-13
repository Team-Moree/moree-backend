from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        authorization_header = request.headers.get("Authorization")

        if authorization_header is None:
            return False

        if not authorization_header.startswith("Bearer "):
            return False

        user_access_token = authorization_header[7:]

        return False
