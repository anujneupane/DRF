from django.contrib import admin
from .models import Record

# Register your models here.

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['name','roll','city','passby']
    
