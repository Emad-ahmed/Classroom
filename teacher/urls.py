from django.urls import path
from .views import TeacherHome, CreateClassview, ClassShow
urlpatterns = [
    path('', TeacherHome.as_view(), name='home'),
    path('create', CreateClassview.as_view(), name='create'),
    path('classshow/<int:id>/', ClassShow.as_view(), name='classshow'),
]
