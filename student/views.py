from django.shortcuts import render
from django.views import View

# Create your views here.


class StudentHome(View):
    def get(self, request):
        return render(request, 'student_home.html')
