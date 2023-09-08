from django.db import models
from django.contrib.auth.models import User,AbstractUser,PermissionsMixin,BaseUserManager,AbstractBaseUser

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class UserProfileManager(BaseUserManager):
    def create_user(self,username,email,phone_no,Role,password=None):
        if not email:
            raise ValueError("Please Provide a email")
        email=self.normalize_email(email)
        print(email)
        user=self.model(username=username,email=email,phone_no=phone_no,Role=Role)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,username,email,phone_no,Role,password):
        user=self.create_user(username,email,phone_no,Role,password)
        user.is_superuser=True
        user.is_staff=True
        user.save()
        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=100,null=True,unique=True)
    phone_no=models.CharField(max_length=10)
    Role=models.CharField(max_length=100,default="")
    email=models.EmailField(max_length=100,unique=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_creator=models.BooleanField(default=False)
    is_moderator=models.BooleanField(default=False)
    is_commenter=models.BooleanField(default=False)
    
    objects=UserProfileManager()
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['phone_no','email','Role']
    

    def __str__(self):
        return self.email

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    class Meta:
        permissions = [
            ("can_create", "Can create new objects"),
            ("can_read", "Can read objects"),
            ("can_update", "Can update objects"),
            ("can_delete", "Can delete objects"),
        ]
    
    
