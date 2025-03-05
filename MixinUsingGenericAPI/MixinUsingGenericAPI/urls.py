from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('crd/<int:pk>', views.StudentList.as_view()),
    # path('crd/', views.Studentcreate.as_view()),
    # path('crd/<int:pk>', views.Studentretrive.as_view()),
    path('crd/<int:pk>', views.StudentUpdate.as_view()),
]
