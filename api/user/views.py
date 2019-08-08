from django.shortcuts import render
from .models import UserSignUp
from rest_framework import generics
from .serializers import UserSignUpSerializer

# Create your views here.

class RegisteredUsersView(generics.ListAPIView):
    queryset = UserSignUp.objects.all()
    serializer_class = UserSignUpSerializer