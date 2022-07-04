from django.shortcuts import redirect, render
from django.views import View
from .models import CreateClass
from .forms import CreateClassForm
from django.contrib import messages
# Create your views here.


class TeacherHome(View):
    def get(self, request):
        if request.user.is_authenticated:
            create = CreateClass.objects.filter(user=request.user)
            return render(request, 'teacher_home.html', {'create': create})
        else:
            return redirect("/")


class CreateClassview(View):
    def get(self, request):
        if request.user.is_authenticated:
            fm = CreateClassForm()
            return render(request, 'createclass.html', {'form': fm})
        else:
            return redirect("/")

    def post(self, request):
        fm = CreateClassForm(request.POST)
        if fm.is_valid():
            obj = fm.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, "Successfully Saved")
        else:
            messages.success(request, "Failed To Saved")
        return render(request, 'createclass.html', {'form': fm})


class ClassShow(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            classshow = CreateClass.objects.get(pk=id)
            return render(request, 'classview.html', {'classshow': classshow})
        else:
            return redirect("/")
