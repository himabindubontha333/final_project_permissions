from books.api import api_view
from books.schema_definitions.create_book_schema import CreateBookSchema
from books.config import CREATE_BOOKS_API
from books.models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from books.models import Book
from books.serializers import BookSerializer
from rest_framework import status

from rest_framework import permissions
from books.permissions import *

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request, so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the object.
        return obj.owner == request.user

@api_view(['POST'])
@permission_classes([IsAuthenticated,IsOwnerOrReadOnly,AdminPermission])
def create_book(request):
    if request.user.has_perm('books.add_book'):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'detail': 'You do not have permission to create a book.'}, status=status.HTTP_403_FORBIDDEN)








