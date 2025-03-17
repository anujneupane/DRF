from django.shortcuts import render
from .serializer import RecordSerializer
from rest_framework.generics import ListAPIView
from .models import Record

# Create your views here.
class RecoredApi(ListAPIView):
    serializer_class = RecordSerializer
    queryset = Record.objects.all()
    def get_queryset(self):
        user = self.request.user
        return Record.objects.filter(passby = user)
