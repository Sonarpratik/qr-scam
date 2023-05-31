# from django.contrib import admin
from django.urls import path,include
# from api.views import *
# from api import views
from rest_framework import routers

router=routers.DefaultRouter()

from app import views


urlpatterns = [
    path('',include(router.urls)),
    # path('home/',home),
    # path('student/',post_student),
    # path('update-student/<id>/',update_student),
    # path('delete-student/<id>/',delete_student),
    # path('get-book/',get_book),
    # path('get-cat/',get_cat),
    
    # path('student/',StudentAPI.as_view()),
    path('stuinfo/<int:pk>/',views.student_detail),
    path('stuinfo/',views.student_list),

]
