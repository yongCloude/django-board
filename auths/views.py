from django.shortcuts import render
from rest_framework import generics

from .serializers import ResisterSerializer

# Create your views here.
class RegisterView(generics.CreateAPIView) :
    queryset = User.objects.all()
    serializer_class = ResisterSerializer
    

