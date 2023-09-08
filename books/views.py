from django.shortcuts import render
from rest_framework import viewsets
from .models import Author, Book,UserProfile
from .serializers import AuthorSerializer, BookSerializer
from .permissions import *

# Create your views here.

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminOrReadOnly]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action == 'list':
            # Allow list view to all authenticated users
            return [permissions.IsAuthenticated()]
        elif self.action == 'create':
            # Allow creation only for authenticated users with Creator role
            return [CanCreateBook()]
        elif self.action == 'retrieve':
            # Allow read operation based on custom permissions
            return [CanReadBook()]  # Adjust for other roles
        elif self.action == 'update':
            # Allow update based on custom permissions
            return [CanUpdateBook()]  # Adjust for other roles
        elif self.action == 'partial_update':
            # Allow partial update based on custom permissions
            return [CanUpdateBook()]  # Adjust for other roles
        elif self.action == 'destroy':
            # Allow delete based on custom permissions
            return [CanDeleteBook()]  # Adjust for other roles
        return [permissions.IsAuthenticated()]  # Default to authenticated users

    





'''
    def get_permissions(self,pk=None):
        
        # Define a list of permission classes based on user roles
        if self.action in ['create', 'update', 'partial_update']:
            # Users with "Creator" or "Admin" roles can create and update
            permission_classes = [permissions.IsAuthenticated & (permissions.IsAdminUser | CreatorPermission)]
        elif self.action == 'destroy' and pk!=None and UserProfile.objects.filter(pk=Book.objects.get(pk=pk).user)[0].Role=='Admin':
            # Only users with "Admin" role can delete
            permission_classes = [permissions.IsAdminUser & AdminPermission]
        else:
            # All authenticated users can read (list and retrieve)
            permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in permission_classes]
'''
  

        







'''
    def get_permissions(self):
        if self.action == 'create':
            return [AdminPermission(),CreatorPermission()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [AdminPermission(), ModeratorPermission(), CreatorPermission()]
        elif self.action == 'list':
            return [AdminPermission(),CommentorPermission(), ModeratorPermission(), CreatorPermission()]
        else:
            return [AdminPermission(),CreatorPermission(), ModeratorPermission(), CommentorPermission()]
    
'''