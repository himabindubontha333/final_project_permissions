from books.api import books_api
from books.schema_definitions.create_book_schema import deleteBookSchema
from books.config import DELETE_BOOKS_API
from rest_framework import permissions


class CanReadBook(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return True  