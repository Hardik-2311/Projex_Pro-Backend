from rest_framework.permissions import IsAuthenticated

class IsSessionAuthenticated(IsAuthenticated):
    """
    Custom permission class for session authentication.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    



