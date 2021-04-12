from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


# Create your models here.

class Users_Manager(BaseUserManager):
    def create_user(self,email,phone,name,password=None):
        # if not email:
        #     raise ValueError ("Email is required")

        # if not phone:
        #     raise ValueError ("Phone Number is required")

        # if not name:
        #     raise ValueError ("Name  is required")
        
        user = self.model(email = self.normalize_email(email),
                          phone = phone,
                          name = name )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self,email,phone,name,password=None):
        user = self.create_user(email = self.normalize_email(email),
                          phone = phone,
                          name = name,
                          password=password )
        user.save(using = self._db)

        
    
class User(AbstractBaseUser):
    name = models.CharField(max_length=50,null=False,blank=False)
    email= models.EmailField(max_length = 50,null=False,blank=False,unique=True)
    phone= models.CharField(max_length=10,null=False,blank=False)
    password= models.CharField(max_length=1024,null=False,blank=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","phone"]

    objects = Users_Manager()

    def __str__(self):
        return self.email



