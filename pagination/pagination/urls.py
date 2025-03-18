from django.contrib import admin
from django.urls import path
from api.views import userList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',userList.as_view()),
]
