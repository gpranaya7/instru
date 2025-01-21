from django.db import models

# Create your models here.
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser,BaseUserManager
from rest_framework_simplejwt.tokens import RefreshToken
class CustomUserManager(BaseUserManager):
    
    def create_user(self,email,username,first_name,last_name,password):
        if not email:
            raise ValueError('email is not given')
        nemail=self.normalize_email(email)
        uo=self.model(email=nemail,username=username,first_name=first_name,last_name=last_name)
        uo.set_password(password)
        uo.save()
        return uo

    
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
    objects=CustomUserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name','username']
    def __str__(self):
        return self.email
    def tokens(self):
        refresh=RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }


