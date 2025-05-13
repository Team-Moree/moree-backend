from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        admin_session_id = request.COOKIES.get("admin-session-id")
        return False
