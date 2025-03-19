from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .form import Student
from .models import user
from django.shortcuts import redirect
from django.views.generic import TemplateView,View
from django.views.generic.base import RedirectView

class Add(TemplateView):
    template_name = 'start/addandshow.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = Student()
        stud = user.objects.all()
        context['form']=fm
        context['data']=stud
        return context
    
    def post(self,request):
        fm = Student(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,'New Data Added')
            fm = Student()
            return redirect('/')
        else:
            fm = Student()
            stud = user.objects.all()
            return render(request,'start/addandshow.html',{'form':fm,'data':stud})

# Create your views here.
# def Add(request):
#     if request.method =='POST':
#         fm = Student(request.POST)
#         if fm.is_valid():
#             fm.save()
#             messages.add_message(request,messages.SUCCESS,'New Data Added')
#             fm = Student()
#         return redirect('/')
#     else:
#         fm = Student()
#     stud = user.objects.all()
#     return render(request,'start/addandshow.html',{'form':fm,'data':stud})
 

class delete(RedirectView):
    url = '/'
    def get_redirect_url(self,*args,**kwargs):
        dt= kwargs['id']
        user.objects.get(pk=dt).delete()
        return super().get_redirect_url(*args,**kwargs)
    

    
      
# def delete(request,id):
#      if request.method =='POST':
#          dl = user.objects.get(pk=id)
#          dl.delete()
#          return HttpResponseRedirect('/')
     


class update(View):
    template_name = 'start/update.html'
    def get(self, request,id):
          pi = user.objects.get(pk=id)
          fm = Student(instance = pi)
          return render(request, self.template_name,{'form':fm})
    
    def post(self,request,id):
        pi = user.objects.get(pk=id)
        fm = Student(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')

# def update(request,id): 
#     if request.method =='POST':
#         pi = user.objects.get(pk=id)
#         fm = Student(request.POST,instance=pi)
#         if fm.is_valid():
#             fm.save()
#             return HttpResponseRedirect('/')
#     else:
#         pi = user.objects.get(pk=id)
#         fm = Student(instance = pi)
        
#     return render(request, 'start/update.html',{'form':fm})
    
    
