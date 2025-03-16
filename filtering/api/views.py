from django.shortcuts import render
from .serializer import RecordSerializer
from rest_framework.generics import ListAPIView

# Create your views here.
class RecoredApi(ListAPIView):
    serializer_class = RecordsSerializer
    queryset = Record.objects.all()
