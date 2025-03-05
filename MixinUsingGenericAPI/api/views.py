from .models import student
from .serializer import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin    
 
class StudentList(GenericAPIView,ListModelMixin):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
class Studentcreate(GenericAPIView,CreateModelMixin):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class Studentretrive(GenericAPIView,RetrieveModelMixin):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
class StudentUpdate(GenericAPIView,UpdateModelMixin):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)    