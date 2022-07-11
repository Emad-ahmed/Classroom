from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from datetime import datetime


Choice_Type = (
    ('Assignment', 'Assignment'),
    ('Presentation', 'Presentation'),
    ('Exam Info', 'Exam Info'),
)


class CreateClass(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class_code_name = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    subject_name = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    classcode = models.CharField(max_length=100)

    def __str__(self):
        return self.class_code_name


class Announcement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    classview = models.ForeignKey(CreateClass, on_delete=models.CASCADE)
    text = models.TextField()


Choice_Type = (
    ('Assignment', 'Assignment'),
    ('Presentation', 'Presentation'),
    ('Exam Info', 'Exam Info'),
)


class AddClassWork(models.Model):
    myclass = models.ForeignKey(
        CreateClass, on_delete=models.CASCADE)
    mytopic = models.CharField(
        max_length=20, choices=Choice_Type, default='Presentation')
    title = models.TextField(max_length=100, default="none")
    description = models.TextField(blank=True, null=True)
    marks = models.IntegerField(blank=True, null=True, default=10)
    imagephoto = models.ImageField(upload_to='images/', blank=True, null=True)
    document = models.FileField(upload_to='documents/', blank=True, null=True)
    current_date = models.DateTimeField(
        auto_now_add=True,  blank=True)
    end_date_time = models.DateTimeField(blank=True, null=True)


# Create your models here.

class QuesModel(models.Model):
    myclass = models.ForeignKey(
        CreateClass, on_delete=models.CASCADE, null=True)

    topics = models.CharField(max_length=200, default="new")
    question = models.CharField(max_length=200, null=True)
    op1 = models.CharField(max_length=200, null=True)
    op2 = models.CharField(max_length=200, null=True)
    op3 = models.CharField(max_length=200, null=True)
    op4 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.question
