from django.shortcuts import render
from rest_framework import viewsets
from .serializer import UserSerializer
from .models import User
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class userViewSets(viewsets.ViewSet):
    def List(self,request):
        user = User.objects.all()
        serializer = UserSerializer(user,many = True)
        return Response(serializer.data)
    
    def retrive(self,request,pk=None):
        if pk is not None:
            user = User.objects.get(id = pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
    
    def create(self,request):
        serial = UserSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response({'msg':'Data Created'},status = status.HTTP_201_CREATED)
        return Response(serial.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk):
        id = pk
        user = user.objects.get(pk = id)
        serial = UserSerializer(user,data = request.data)
        if serial.is_valid():
            serial.save()
            return Response({'msg':'Complate Data Updated'})
        return Response(serial.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        id = pk
        user = user.objects.get(pk = id)
        serial = UserSerializer(user,data = request.data,partial = True)
        if serial.is_valid():
            serial.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serial.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk):
        id = pk
        user = user.objects.get(pk = id)
        user.delete()
        return Response({'msg': 'Data Deleted'})


