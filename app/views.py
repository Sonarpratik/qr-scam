from .models import *
from .serializers import *
from rest_framework import generics
# from djoser import views
from djoser import views
from django.http import JsonResponse

from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework.permissions import IsAuthenticated

class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

class CustomPasswordResetView(views.UserViewSet):
    def send_email(self, *args, **kwargs):
        response = super().send_email(*args, **kwargs)

        # Customize the response here
        data = {
            'message': 'Password reset email has been sent successfully.',
            'status_code': response.status_code,
        }

        return JsonResponse(data)
    
from rest_framework.response import Response
from rest_framework.decorators import api_view

#multiple
@api_view(["GET"])
def userinfo2(request):
    user = request.user
    if user.is_authenticated:
        profile = UserProfile.objects.get(user=user)
        roles = []

        if profile.is_staff:
            roles.append("STAFF")
        if profile.is_admin:
            roles.append("ADMIN")
        if profile.is_customer:
            roles.append("CUSTOMER")
        

        if roles:
            data = {"user": user.username, "email": user.email, "roles": roles}
            return Response(data)
        else:
            return Response({"message": "you are not assigned any roles"})
    else:
        return Response({"message": "login first"})
    

#single
@api_view(["GET"])
def userinfo(request):
    user = request.user
    if user.is_authenticated:
        profile = UserProfile.objects.get(user=user)
        if profile.is_admin == True:
            data = {"username": user.username, "email": user.email, "roll": "ADMIN"}
            return Response(data)
        elif profile.is_staff == True:
            data = {"username": user.username, "email": user.email, "roll": "STAFF"}
            return Response(data)
        elif profile.is_customer == True:
            data = {"username": user.username, "email": user.email, "roll": "CUSTOMER"}
            return Response(data)
      
       
        else:
            data = {"message": "you are not valid user"}
            return Response(data)
    else:
        return Response({"message": "login first"})
