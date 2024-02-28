


from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser

class UserAccount(AbstractUser):
    
    name = models.CharField(max_length=100, blank=True,null=True)
    email = models.CharField(max_length=100, blank=True,null=True)
    username = models.CharField(max_length=100, unique=True)
    phonenumber = models.CharField(max_length=100,blank=True,null=True)
    access_for=models.CharField(max_length=100, blank=True,null=True)
    is_superuser = models.BooleanField(default=False)
    # is_super = models.BooleanField(default=False)
    
    education = models.BooleanField(default=False)
    career = models.BooleanField(default=False)
    micro_bussiness = models.BooleanField(default=False)
    spritual = models.BooleanField(default=False)
    
    # is_super = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    def __str__(self):
        return self.username
from django.contrib.auth.admin import UserAdmin
class UserAccountAdmin(UserAdmin):
    model = UserAccount

    # Define the fieldsets with custom permissions
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('name', 'email', 'phonenumber',"access_for")}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_customer')}),
        ('Services', {'fields': ('education', 'career', 'micro_bussiness', 'spritual')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
class UserProfile(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    # is_cutting = models.BooleanField(default=False)
    # is_production = models.BooleanField(default=False)
    # is_accountent = models.BooleanField(default=False)
    # is_admin = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username


