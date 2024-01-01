


from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    # is_cutting = models.BooleanField(default=False)
    # is_production = models.BooleanField(default=False)
    # is_accountent = models.BooleanField(default=False)
    # is_admin = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
