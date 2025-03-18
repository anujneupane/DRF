from django.shortcuts import render
from .serializer import RecordSerializer
from rest_framework.generics import ListAPIView
from .models import Record
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
# Create your views here.
class RecoredApi(ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    #filter_backends = [DjangoFilterBackend] 
    #filterset_fields = ['passby','city','roll']
    filter_backends = [SearchFilter] 
    #search_fields = ['city','name']
    search_fields = ['^city','^name']  # ^ for start with of city and name

    ''' def get_queryset(self):
        user = self.request.user
        return Record.objects.filter(passby = user) '''
