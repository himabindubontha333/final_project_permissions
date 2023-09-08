from books.api import books_api
from books.schema_definitions.create_book_schema import deleteBookSchema
from books.config import DELETE_BOOKS_API
from books.models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from books.permissions import *

@permission_classes([IsAuthenticated,AdminPermission])
@books_api.get(DELETE_BOOKS_API,data=deleteBookSchema)
def DELETE_BOOKS_API(request,data=deleteBookSchema):
    pass