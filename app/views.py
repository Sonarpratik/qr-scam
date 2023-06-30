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