from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api.views import *
router = DefaultRouter() 
router.register('singer', Singerviewset, basename='singer')
router.register('song', Songviewset, basename='song')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
