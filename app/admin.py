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
from django.contrib import admin

# Register your models here.

# admin.site.register(Student)
# admin.site.register(Book)
# admin.site.register(Category)
# admin.site.register(Song)
# admin.site.register(UserAccount)
admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(DocModel)
# admin.site.register(Singer)
admin.site.site_header="Aumbeeco"
admin.site.site_title="Aumbeeco"
admin.site.index_title="Aumbeeco"