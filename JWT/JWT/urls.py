from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView 


router = DefaultRouter()
router.register('userapi',views.UserModelViewSet,basename ='user')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain'),
    path('token_refresh/',TokenRefreshView.as_view(),name='token_ref'),
    path('token_verify/',TokenVerifyView.as_view(),name='token_veri'),
]

