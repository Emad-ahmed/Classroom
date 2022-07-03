from django.shortcuts import render
from django.views import View

# Create your views here.


class TeacherHome(View):
    def get(self, request):
        return render(request, 'teacher_home.html')
