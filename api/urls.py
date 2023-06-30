from django.contrib import admin
from django.urls import path,include
from api.views import *
from api import views
from rest_framework import routers

router=routers.DefaultRouter()
# router.register(r'companies',ComapnyViewSet)
# 
# router.register('singer',views.SingerViewSet,basename='singer')
# router.register('song',views.SongViewSet,basename='song')
router.register('invoice',views.InvoiceViewSet,basename='invoice')
router.register('user',views.UserViewSet,basename='user')

router.register('proforminvoice',views.ProformInvoiceViewSet,basename='proforminvoice')
router.register('proformuser',views.ProformUserViewSet,basename='proformuser')

router.register('client',views.ClientViewSet,basename='client')
# router.register('shipping',views.ShippingViewSet,basename='shipping')

router.register('inventory',views.InventoysViewSet,basename='inventory')


urlpatterns = [
    path('',include(router.urls)),
    # path('home/',home),
    # path('student/',post_student),
    # path('update-student/<id>/',update_student),
    # path('delete-student/<id>/',delete_student),
    # path('get-book/',get_book),
    # path('get-cat/',get_cat),
    # path(r'auth/', include('djoser.urls')),
    # path(r'auth/', include('djoser.urls.jwt')),
    
    #  path(r'auth/webauthn/', include('djoser.webauthn.urls')),
    # path('student/',StudentAPI.as_view()),
    # path('userinfo', views.userinfo, name="userinfo"),
    # path('inven',views.,name='inven')


]
