from rest_framework.permissions import BasePermission

class IsLandlord(BasePermission):
    """
    Allows access only to users with role 'landlord'.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'landlord'


class IsTenant(BasePermission):
    """
    Allows access only to users with role 'tenant'.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'tenant'
