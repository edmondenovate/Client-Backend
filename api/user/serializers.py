from rest_framework import serializers
from .models import UserSignUp

class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSignUp
        fields = ("names", "email", "password")