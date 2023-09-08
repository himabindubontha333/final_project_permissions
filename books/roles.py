# your_app_name/roles.py

from django.contrib.auth.models import Group

admin_group, created = Group.objects.get_or_create(name='Admin')
creator_group, created = Group.objects.get_or_create(name='Creator')
commentor_group, created = Group.objects.get_or_create(name='Commentor')
moderator_group, created = Group.objects.get_or_create(name='Moderator')
