from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return any([
            request.method in permissions.SAFE_METHODS,
            obj.author == request.user,
        ])
