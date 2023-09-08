from books.api import books_api
from books.schema_definitions.create_book_schema import ViewBookSchema
from books.config import VIEW_BOOKS_API
from rest_framework import permissions

class CanDeleteBook(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and (
            request.user.Role == 'Moderator' or request.user.Role == 'Admin' or request.user.Role=='Moderator'
        )  