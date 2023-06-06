from django.contrib import admin

# Register your models here.

from .models import *
# admin.site.register(Student)
# admin.site.register(Book)
# admin.site.register(Category)
# admin.site.register(Song)
# admin.site.register(Singer)
admin.site.site_header="Balaji Steel"
admin.site.site_title="Balaji Steel"
admin.site.index_title="Balaji Steel"
admin.site.register(Invoice)
admin.site.register(User)
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
 list_display=['id','name','company_name']

# @admin.register(Inventorys)
# class InventorysAdmin(admin.ModelAdmin):
#  list_display=['id','sac','rate']
# admin.site.register(Shipping)