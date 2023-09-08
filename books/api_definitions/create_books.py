from books.api import api_view
from books.schema_definitions.create_book_schema import CreateBookSchema
from books.config import CREATE_BOOKS_API
from rest_framework import permissions

class CanCreateBook(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is allowed to create a book
        return request.user.is_authenticated and request.user.Role == 'Creator' or request.user.Role=='Admin'









