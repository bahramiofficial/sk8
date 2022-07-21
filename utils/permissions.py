from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    message = 'premission denid, you are not Owner'

    # def has_permission(self, request, view):
    #     return True # request.user.is_authrnticated and request.user  # check login user

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user


#drf-sepctacular