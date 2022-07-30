from email import message
from pickle import NONE
from django.shortcuts import redirect, render
from django.views import View

from mainapp.models import Student
from .models import JoinClass
from teacher.models import CreateClass
# Create your views here.
from django.contrib import messages


class StudentHome(View):
    def get(self, request):
        student = request.session.get("student")
        if student:
            studentuser = Student.objects.get(pk=student)
            classview = JoinClass.objects.filter(student=studentuser)
            return render(request, 'student_home.html', {'classview': classview})
        else:
            return redirect("/")


class JoinClassView(View):
    def get(self, request):
        student = request.session.get("student")
        if student:
            allclass = JoinClass.objects.filter()
            return render(request, 'joinclass.html')
        else:
            return redirect("/")

    def post(self, request):
        student = request.session.get("student")
        class_code = request.POST.get("class_code")
        studentuser = Student.objects.get(pk=student)
        try:
            allclass = CreateClass.objects.get(classcode=class_code)
        except:
            allclass = NONE

        classview = JoinClass(student=studentuser, myclass=allclass)

        n = JoinClass.objects.filter(
            student=studentuser, myclass__classcode=class_code)

        if n:
            messages.warning(request, "Class Already Exits")

        else:
            if classview:
                classview.save()
                return redirect("/student")

        return render(request, 'joinclass.html')


class ClassworkView(View):
    def get(self, request, id):
        student = request.session.get("student")
        if student:
            allclass = JoinClass.objects.get(id=id)
            return render(request, 'joinclass.html')
        else:
            return redirect("/")
