# from django.contrib import admin
from django.urls import path,include
from app.views import *
# from api import views
from rest_framework import routers
router=routers.DefaultRouter()

from app import views


urlpatterns = [
    path('',include(router.urls)),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),




]
