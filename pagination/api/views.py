from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import User
from .serializer import UserSerializer


class userList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer