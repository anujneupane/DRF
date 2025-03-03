from django.contrib import admin
from .models import student
# admin.site.register(student)

# Register your models here.
@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']