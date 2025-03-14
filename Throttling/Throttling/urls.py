from django.contrib import admin
from django.urls import path,include

from rest_framework.routers import DefaultRouter
from api.views import UserModelViewSet

router= DefaultRouter()
router.register('userapi',UserModelViewSet,basename ='user')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls', namespace = 'rest_framework'))
]
