from rest_framework import generics


class BaseGenericAPIView(generics.GenericAPIView):
    def check_permissions(self, request):
        """
        Check if the request should be permitted.
        Raises an appropriate exception if the request is not permitted.
        """
        flag = False
        permission = None

        for _permission in self.get_permissions():
            permission = _permission
            if _permission.has_permission(request, self):
                flag = True
                break

        if flag is False:
            self.permission_denied(
                request,
                message=getattr(permission, 'message', None),
                code=getattr(permission, 'code', None)
            )

    def check_object_permissions(self, request, obj):
        """
        Check if the request should be permitted for a given object.
        Raises an appropriate exception if the request is not permitted.
        """
        flag = False
        permission = None

        for _permission in self.get_permissions():
            permission = _permission
            if _permission.has_object_permission(request, self, obj):
                flag = True
                break

        if flag is False:
            self.permission_denied(
                request,
                message=getattr(permission, 'message', None),
                code=getattr(permission, 'code', None)
            )
