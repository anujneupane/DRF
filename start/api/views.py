from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializer import serial
import io
from rest_framework.renderers import JSONRenderer
from .models import Student
from django.http import HttpResponse
# Create your views here.

@csrf_exempt
def stu(request):
    if request.method =='GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            stu =Student.objects.get(id=id)
            serializer = serial(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')

    stu = Student.objects.all()
    serializer = serial(stu,many= True) 
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type ='application/json')


