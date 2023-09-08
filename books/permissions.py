from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.has_perm('books.admin_permission'):
            return True
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.user.has_perm('books.admin_permission'):
            return True
        return request.method in permissions.SAFE_METHODS or (
            request.method in ['PUT', 'PATCH', 'DELETE']
        )


class CanCreateBook(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is allowed to create a book
        return request.user.is_authenticated and request.user.Role == 'Creator' or request.user.Role=='Admin'

class CanReadBook(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is allowed to read the book (e.g., Creator, Admin, etc.)
        return True  # Adjust this logic as needed

class CanUpdateBook(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is allowed to update the book
        return request.user.is_authenticated and request.user.Role == 'Creator' or request.user.Role=='Admin' or request.user.Role=='Moderator'

class CanDeleteBook(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is allowed to delete the book (e.g., Creator, Admin, etc.)
        return request.user.is_authenticated and (
            request.user.Role == 'Moderator' or request.user.Role == 'Admin' or request.user.Role=='Moderator'
        )  # Adjust as needed for other roles
