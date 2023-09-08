from books.api import books_api
from books.schema_definitions.create_book_schema import ViewBookSchema
from books.config import VIEW_BOOKS_API
from books.models import *
from rest_framework.decorators import api_view, permission_classes
from books.permissions import *

from rest_framework.permissions import IsAuthenticated


@permission_classes([IsAuthenticated,IsOwnerOrReadOnly,AdminPermission])
@books_api.get(VIEW_BOOKS_API,data=ViewBookSchema)
def VIEW_BOOKS_API(request, data=ViewBookSchema):
       try:
         user_Model = UserProfile.objects.get(user=request.user)
         return user_Model.can_view_books
       except UserProfile.DoesNotExist:
            return False