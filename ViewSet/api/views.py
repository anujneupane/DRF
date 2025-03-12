from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializer import UserSerializer
from .models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

