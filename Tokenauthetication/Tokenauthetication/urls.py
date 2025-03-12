from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter() #creating default router object
# router.register('userapi',views.userViewSet,basename ='user')
router.register('userapi',views.UserModelViewSet,basename ='user')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('gettoken/',obtain_auth_token)
]

