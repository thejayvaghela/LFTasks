from django.db import models
from django.contrib.auth.models import AbstractBaseUser,UserManager,BaseUserManager,PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField


class CustomManager(BaseUserManager):
    def create_user(self,mobileNo,first_name,password=None):
        if not mobileNo:
            raise ValueError("Mobile No is required")
        if not first_name:
            raise ValueError("First Name is required")
        user=self.model(mobileNo=mobileNo,first_name=first_name)
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self,mobileNo,first_name,password):
        user=self.create_user(mobileNo=mobileNo,first_name=first_name,password=password)
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser,PermissionsMixin):
    # id (django default), password, first_name, last_login, is_admin, is_active, is_staff, is_superuser, mobileNo, address.
    # Required Fields
    mobileNo=PhoneNumberField(unique=True)
    # username=models.CharField(unique=True,max_length=50) # Username is email. Login with this
    password=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    last_login=models.DateTimeField(auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    address=models.CharField(max_length=500)
    
    objects = CustomManager()
    
    USERNAME_FIELD='mobileNo'
    REQUIRED_FIELDS=['first_name']
    
    def __str__(self):
        return self.first_name
