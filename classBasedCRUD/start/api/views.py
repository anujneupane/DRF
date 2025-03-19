from start.models import user
from start.api.serializer import userserializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class userViewset(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userserializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    