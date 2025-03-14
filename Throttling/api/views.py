from rest_framework import viewsets
from .serializer import UserSerializer
from .models import User
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

