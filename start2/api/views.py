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
        serializer = serial(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        se = serial(data = pythondata)
        if se.is_valid():
            se.save()
            msg = {'msg':'data Inserted through Api'}
            json_data= JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
            # return JsonResponse(msg)
        json_data = JSONRenderer().render(se.errors)
        return HttpResponse(json_data,content_type='application/json')

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        se= serial(stu, data = pythondata, partial = True)
        if se.is_valid():
            se.save()
            msg = {'msg':'Data Updated Successfully through Api'}
            json_data= JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data= JSONRenderer().render(se.errors)
        return HttpResponse(json_data, content_type='application/json')