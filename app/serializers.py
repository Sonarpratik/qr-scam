from rest_framework import serializers
# from app.models import *
from djoser.serializers import UserCreateSerializer,SendEmailResetSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model=User
        fields=('id','username','email','is_active','is_staff')
        

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance
    




class CustomSendEmailResetSerializer(SendEmailResetSerializer):
    print("panner")
    print(SendEmailResetSerializer)

    def save(self):
        # Custom logic for saving the reset email
        # You can modify this method according to your requirements
        print("panneer")

        user = self.user
        print("dfsbdfhsbdsdbsdjfhb")
        print(user)
        user.send_reset_password_email()  # Custom method to send the reset email

    def get_email_options(self):
        # Custom logic for getting email options
        # You can modify this method according to your requirements
        email_options = super().get_email_options()
        # Modify email options here if needed
        print("panneer")

        return email_options
    def post(self):
   
        return print("alpha")