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
router.register('quotation',views.QuotationViewSet,basename='quotation')
router.register('item',views.ItemViewSet,basename='item')

router.register('client',views.ClientViewSet,basename='client')
# router.register('shipping',views.ShippingViewSet,basename='shipping')

router.register('inventory',views.InventoysViewSet,basename='inventory')


urlpatterns = [
    path('',include(router.urls)),
]