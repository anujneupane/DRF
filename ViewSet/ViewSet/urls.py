from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter() #creating default router object
# router.register('userapi',views.userViewSet,basename ='user')
router.register('userapi',views.UserModelViewSet,basename ='user')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]

