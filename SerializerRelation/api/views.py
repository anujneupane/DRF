from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from .models import *

class Singerviewset(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerial


class Songviewset(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerial

