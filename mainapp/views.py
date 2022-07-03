from django.shortcuts import render
from django.views import View

# Create your views here.


class LoginTeacherView(View):
    def get(self, request):
        return render(request, 'login_teacher.html')


class LoginStudentView(View):
    def get(self, request):
        return render(request, 'login_student.html')


class RegisterTeacherView(View):
    def get(self, request):
        return render(request, 'register_teacher.html')


class RegisterStudentView(View):
    def get(self, request):
        return render(request, 'register_student.html')
