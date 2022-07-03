from django.urls import path
from .views import TeacherHome, CreateClassview
urlpatterns = [
    path('', TeacherHome.as_view(), name='home'),
    path('create', CreateClassview.as_view(), name='create'),

]
