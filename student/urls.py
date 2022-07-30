from django.urls import path
from .views import StudentHome, JoinClassView
urlpatterns = [
    path('', StudentHome.as_view(), name='home'),
    path('join_class', JoinClassView.as_view(), name='join_class'),
    path('class_view_work/<int:id>/',
         JoinClassView.as_view(), name='join_class'),
]
