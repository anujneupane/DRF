from .models import student
from .serializer import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin  
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
'''class LC(ListCreateAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

class RUD(RetrieveUpdateDestroyAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

class RU(RetrieveUpdateAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

class RD(RetrieveDestroyAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer  ''' 


  #pk not required for list and create
class StudentLC(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
# retrieve,update,destroy required pk
class StudentRUD(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)    

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)        


