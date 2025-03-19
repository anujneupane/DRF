from django.contrib import admin
from django.urls import path, include
from start.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('crud',views.userViewset,basename='crud')

urlpatterns = [
    path('',include(router.urls))
]

