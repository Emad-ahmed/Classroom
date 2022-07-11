from ast import Return
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.views import View

from mainapp.forms import SignForm
from .models import CreateClass, Announcement, AddClassWork
from .forms import AnnouncementForm, CreateClassForm, AddClassWorkForm, MyPasswordChangeForm, QuesModelForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound


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
            mainid = id
            classshow = CreateClass.objects.get(pk=id)
            allannouce = Announcement.objects.filter(classview=classshow)[::-1]
            return render(request, 'classview.html', {'classshow': classshow, "mainid": mainid, 'allannouce': allannouce})
        else:
            return redirect("/")

    def post(self, request, id):
        mainid = id
        classshow = CreateClass.objects.get(pk=id)

        allannouce = Announcement.objects.filter(classview=classshow)[::-1]
        myuser = request.user
        annouce = request.POST.get("annouce")
        print(annouce)
        annoucesave = Announcement(
            user=myuser, classview=classshow, text=annouce)
        annoucesave.save()
        messages.success(request, "Successfully Saved")
        return render(request, 'classview.html', {'classshow': classshow, "mainid": mainid,  'allannouce': allannouce})


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
            mainid = id
            classshow = CreateClass.objects.get(pk=id)
            allwork = AddClassWork.objects.filter(myclass=classshow)[::-1]
            fm = AddClassWorkForm()
            return render(request, 'add_work.html', {'form': fm, "mainid": mainid,  'allwork': allwork})
        else:
            return redirect("/")

    def post(self, request, id):
        mainid = id
        fm = AddClassWorkForm(request.POST, request.FILES)

        classv = CreateClass.objects.get(pk=id)

        allwork = AddClassWork.objects.filter(myclass=classv)[::-1]
        if fm.is_valid():
            obj = fm.save(commit=False)
            obj.myclass = classv
            obj.save()
            messages.success(request, "Successfully Saved")
        else:
            messages.warning(request, "Failed To Saved")
        return render(request, 'add_work.html', {'form': fm, "mainid": mainid,   "allwork": allwork})


class ShowWorkview(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            allwork = AddClassWork.objects.get(pk=id)
            return render(request, 'ShowWork.html', {'allwork': allwork})
        else:
            return redirect("/")


class PasswordChangeView(View):
    def get(self, request):
        form = MyPasswordChangeForm(user=request.user)

        return render(request, 'passwordchange.html', {'form': form})

    def post(self, request):
        form = MyPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Changed")
            return redirect("/")
        else:
            messages.error(request, "Please Enter Valid Password")
            return render(request, 'passwordchange.html', {'form': form})


class UpdateAccountView(View):
    def get(self, request):
        form = SignForm(instance=request.user)
        return render(request, 'upadte_account.html', {'form': form})


class EditworkView(View):
    def get(self, request, id):
        mywork = AddClassWork.objects.get(pk=id)
        form = Announcement(instance=mywork)
        return render(request, 'editwork.html', {'form': form})

    def post(self, request, id):
        mywork = AddClassWork.objects.get(pk=id)
        form = AddClassWorkForm(request.POST, request.FILES, instance=mywork)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Changed")
            return render(request, 'editwork.html', {'form': form})


class ExamView(View):
    def get(self, request, id):
        mainid = id
        form = QuesModelForm()
        mywork = CreateClass.objects.get(pk=id)
        return render(request, 'exam-info.html', {'mainid': id, 'form': form})

    def post(self, request, id):
        mainid = id
        mywork = CreateClass.objects.get(pk=id)
        form = QuesModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.myclass = mywork
            obj.save()
            messages.success(request, "Successfully Saved")
            return render(request, 'exam-info.html', {'form': form, 'mainid': id, })


class EditAnnouceView(View):
    def get(self, request, id):
        mywork = Announcement.objects.get(pk=id)
        form = AnnouncementForm(instance=mywork)
        return render(request, 'editlist.html', {'form': form})

    def post(self, request, id):
        mywork = Announcement.objects.get(pk=id)
        form = AnnouncementForm(request.POST, instance=mywork)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Changed")
            return render(request, 'editlist.html', {'form': form})


def pdf_view(request, id):

    maindata = AddClassWork.objects.get(pk=id)
    mainfile = maindata.document

    fs = FileSystemStorage()
    filename = str(mainfile)

    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            # user will be prompted display the PDF in the browser
            response['Content-Disposition'] = 'inline; filename="filename"'

            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')
