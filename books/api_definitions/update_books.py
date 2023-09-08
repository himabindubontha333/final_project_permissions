from books.api import books_api
from books.schema_definitions.create_book_schema import UpdateBookSchema
from books.config import UPDATE_BOOKS_API
from books.models import *

from books.permissions import *


from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from books.models import Book
from books.permissions import IsOwnerOrReadOnly  # Import your custom permission

@api_view(['PUT'])  # Specify the HTTP method(s) this view will handle
@permission_classes([IsOwnerOrReadOnly,AdminPermission])  # Apply your custom permission class
def UPDATE_BOOKS_API(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=404, data={"detail": "Book not found."})

    # Check object-level permission using the IsOwnerOrReadOnly permission class
    if not request.user.is_staff and not book.owner == request.user:
        return Response(status=403, data={"detail": "You do not have permission to update this book."})

    if request.method == 'PUT':
        # Your update logic here
        # Example: update the book with id=pk
        # book.title = request.data.get('title')
        # book.author = request.data.get('author')
        # book.save()
        return Response({"detail": "Book updated successfully."})
'''
@permission_classes([IsOwnerOrReadOnly])
@books_api.get(UPDATE_BOOKS_API,data=UpdateBookSchema)
def UPDATE_BOOKS_API(request, data=UpdateBookSchema):
       try:
        user_Model = UserProfile.objects.get(user=request.user)
        return user_Model.can_update_books
       except UserProfile.DoesNotExist:
            return False
'''
