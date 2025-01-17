from .models import *
from .serializers import *

# from djoser import views
from djoser import views
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
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
def userinfo(request):
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
    




    
from rest_framework import viewsets, status

class ProfileViewSet(viewsets.ModelViewSet):
    
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
class DocViewSet(viewsets.ModelViewSet):
    
    queryset = DocModel.objects.all()
    serializer_class = DocSerializer

from django.shortcuts import render
from django.contrib.auth.models import User

def get_all_users(request):
    all_users = User.objects.all()
    user_data = [{'id': user.id, 'username': user.username} for user in all_users]
    return JsonResponse({'users': user_data})


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    authentication_classes = [] 
    def perform_create(self, serializer):
        # Set is_active to False by default
        serializer.save()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response( status=status.HTTP_201_CREATED, headers=headers)


# views.py

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from app.models import UserAccount
from app.serializers import UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        
        return self.request.user

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)
