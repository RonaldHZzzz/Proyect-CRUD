from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializers
from rest_framework.permissions import IsAuthenticated, AllowAny


class createUserView(generics.createAPIview):
    queryset= User.objects.all()
    serializer_class=User
    permission_classes=[AllowAny]