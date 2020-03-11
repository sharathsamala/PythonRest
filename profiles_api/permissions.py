from rest_framework import permissions


class UpdateOwnProfiles(permissions.BasePermission):
    """Allow users to edit only their own profiles"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profiles"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


