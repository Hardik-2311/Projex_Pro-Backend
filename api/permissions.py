from rest_framework import permissions

class IsMemberAdminCreator(permissions.BasePermission):
    message = "You don't have permission to perform this action."

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the user has permission to create/update/delete based on project roles
        project_id = view.kwargs.get('project_id')
        user = request.user

        try:
            project = project.objects.get(pk=project_id)

            if user.is_superuser or project.creator == user or project.project_members.filter(username=user.username).exists():
                return True
        except project.DoesNotExist:
            pass

        return False
    
from rest_framework import permissions

class IsAdminToCreateGoal(permissions.BasePermission):
    message = "Only admin users can create goals."
    def has_permission(self, request, view):
        return request.user.is_superuser

from rest_framework import permissions

class IsAdminToPerformFeedbackActions(permissions.BasePermission):
    message = "Only admin users can perform this action."

    def has_permission(self, request, view):
        return request.user.is_superuser

