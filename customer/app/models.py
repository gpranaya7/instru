from django.db import models

# Create your models here.
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser,BaseUserManager


#class CustomUserManager(BaseUserManager):

    
def create_superuser(self,email,username,first_name,last_name,password):
        suo=self.create_user(email,username,first_name,last_name,password)
        suo.is_staff=True
        suo.is_superuser=True
        suo.save()   



class CustomUser(PermissionsMixin,AbstractBaseUser):
    email=models.EmailField(primary_key=True)
    username=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    #objects=CustomUserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name']

