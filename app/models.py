


from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser

class UserAccount(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    phonenumber = models.CharField(max_length=100, unique=True,blank=True,null=True)

    is_superuser = models.BooleanField(default=True)
    # is_super = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_customer = models.BooleanField(default=False)

    def __str__(self):
        return self.username
from django.contrib.auth.admin import UserAdmin
class UserAccountAdmin(UserAdmin):
    model = UserAccount

    # Define the fieldsets with custom permissions
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'phonenumber')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_customer')}),
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


