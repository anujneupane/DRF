from django.contrib import admin
from django.urls import path
from api.views import RecoredApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RecoredApi.as_view()),
]
