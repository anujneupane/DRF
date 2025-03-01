from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crd/', views.testing),
    path('crd/<int:pk>', views.testing),
]
