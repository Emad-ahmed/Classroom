from django.db import models
from teacher.models import CreateClass
from mainapp.models import Student
from teacher.models import Announcement
# Create your models here.


class JoinClass(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    myclass = models.ForeignKey(CreateClass, on_delete=models.CASCADE)


class Comment(models.Model):
    