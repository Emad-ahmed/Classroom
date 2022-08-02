from django.contrib import admin
from .models import JoinClass, CommentMain

# Register your models here.


@admin.register(JoinClass)
class JoinClassadmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(CommentMain)
class CommentMainadmin(admin.ModelAdmin):
    list_display = ['id']
