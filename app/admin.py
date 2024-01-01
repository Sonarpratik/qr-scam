from django.contrib import admin
from .models import *
from .serializers import *
# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(UserProfile)
# # @admin.register(Student)
# # class StudentAdmin(admin.ModelAdmin):
# #  list_display=['id','name','roll','city']
# admin.site.register(UserAccount)
# admin.site.register(UserAccountManager)
