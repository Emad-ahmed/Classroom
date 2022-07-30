from django.contrib import admin
from .models import JoinClass

# Register your models here.


@admin.register(JoinClass)
class JoinClassadmin(admin.ModelAdmin):
    list_display = ['id']
