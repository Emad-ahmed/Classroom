from django.shortcuts import render
from django.views import View
from .models import CreateClass
from .forms import CreateClassForm
# Create your views here.


class TeacherHome(View):
    def get(self, request):
        return render(request, 'teacher_home.html')


class CreateClassview(View):
    def get(self, request):
        fm = CreateClassForm()
        return render(request, 'createclass.html', {'form': fm})
