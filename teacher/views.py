from ast import Return
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.views import View
from .models import CreateClass, Announcement, AddClassWork
from .forms import CreateClassForm, AddClassWorkForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.urls import reverse


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
            messages.warning(request, "Failed To Saved")
        return render(request, 'createclass.html', {'form': fm})


class ClassShow(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            classshow = CreateClass.objects.get(pk=id)
            allannouce = Announcement.objects.filter(classview=classshow)[::-1]
            return render(request, 'classview.html', {'classshow': classshow, 'allannouce': allannouce, "id": id})
        else:
            return redirect("/")

    def post(self, request, id):
        classshow = CreateClass.objects.get(pk=id)
        allannouce = Announcement.objects.filter(classview=classshow)[::-1]
        myuser = request.user
        annouce = request.POST.get("annouce")
        print(annouce)
        annoucesave = Announcement(
            user=myuser, classview=classshow, text=annouce)
        annoucesave.save()
        messages.success(request, "Successfully Saved")
        return render(request, 'classview.html', {'classshow': classshow,  'allannouce': allannouce})


def userlogout(request):
    logout(request)
    return redirect('/')


def deletecard(request, id):
    crea = CreateClass.objects.get(pk=id)
    crea.delete()
    return redirect('/teacher')


def deletelist(request, id):
    ann = Announcement.objects.get(pk=id)
    ann.delete()
    return redirect("/teacher")


def deletework(request, id):
    ann = AddClassWork.objects.get(pk=id)
    ann.delete()
    return redirect("/teacher")


class Addworkview(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            classshow = CreateClass.objects.get(pk=id)
            allwork = AddClassWork.objects.filter(myclass=classshow)[::-1]
            fm = AddClassWorkForm()
            return render(request, 'add_work.html', {'form': fm, 'id': id, 'allwork': allwork})
        else:
            return redirect("/")

    def post(self, request, id):
        fm = AddClassWorkForm(request.POST)

        classv = CreateClass.objects.get(pk=id)

        allwork = AddClassWork.objects.filter(myclass=classv)[::-1]
        if fm.is_valid():
            obj = fm.save(commit=False)
            obj.myclass = classv
            obj.save()
            messages.success(request, "Successfully Saved")
        else:
            messages.warning(request, "Failed To Saved")
        return render(request, 'add_work.html', {'form': fm, 'id': id, "allwork": allwork})
