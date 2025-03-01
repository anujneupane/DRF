from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import student
from .serializer import StudentSerializer
from rest_framework import status
# Create your views here.


# @api_view(['GET','POST'])
# def testing(request):
#     if request.method =='GET':    
#       return Response('Get aayo hai api view bata')
    
#     if request.method =='POST':  
#       print(request.data)  
#       return Response('Post aayo hai api view bata')

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def testing(request , pk=None):
    if request.method =='GET':  
       id = pk #request.data.get('id')
       if id is not None:
           stu = student.objects.get(id=id)
           serial = StudentSerializer(stu)
           return Response(serial.data)
       stu = student.objects.all()
       serial = StudentSerializer(stu,many = True)
       return Response(serial.data)
    
    if request.method =='POST': 
       serial =StudentSerializer(data = request.data)
       if serial.is_valid():
           serial.save()
           return Response({'msg': 'Data Created'},status = status.HTTP_201_CREATED)
       return Response(serial.errors,status = status.HTTP_400_BAD_REQUEST)
    
    if request.method =='PUT':
      id = pk #request.data.get('id')
      stu = student.objects.get(pk=id)
      serial =StudentSerializer(stu,data=request.data)
      if serial.is_valid():
           serial.save()
           return Response({'msg': 'Complete Data Updated'})
      return Response(serial.errors,status = status.HTTP_400_BAD_REQUEST)
    
    if request.method =='PATCH':
      id = pk #request.data.get('id')
      stu = student.objects.get(pk=id)
      serial =StudentSerializer(stu,data=request.data,partial= True)
      if serial.is_valid():
           serial.save()
           return Response({'msg': 'Partial Data Updated'})
      return Response(serial.errors,status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE': 
      id = pk #request.data.get('id')
      stu = student.objects.get(pk=id)
      stu.delete()
      return Response({'msg':'data deleted of id '+str(id)})


       
  

       
     

    