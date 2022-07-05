from django.contrib import admin
from .models import CreateClass, Announcement
# Register your models here.


@admin.register(CreateClass)
class CreateAdmin(admin.ModelAdmin):
    list_display = ['id', "class_code_name", "section", "subject_name"]


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['id']
