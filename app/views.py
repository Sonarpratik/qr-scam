from .models import *
from .serializers import *
from rest_framework import generics

from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework.permissions import IsAuthenticated

class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer