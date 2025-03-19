from django.contrib import admin
from django.urls import path,include
from start import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', views.Add.as_view(), name ='add'),
    path ('update/<int:id>', views.update.as_view(), name ='upt'),
    path ('delete/<int:id>', views.delete.as_view(), name ='dlt'),
    path ('api/', include('start.api.urls'))

]
