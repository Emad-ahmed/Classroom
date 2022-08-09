from django.urls import path
from .views import StudentHome, JoinClassView, ClassworkView, studentlogout, AnnouceView, WorkView
urlpatterns = [
    path('', StudentHome.as_view(), name='home'),
    path('join_class', JoinClassView.as_view(), name='join_class'),
    path('class_view_work/<int:id>/',
         ClassworkView.as_view(), name='class_view_work'),
    path('studentlogout', studentlogout, name='studentlogout'),
    path('annouceview/<int:id>/', AnnouceView.as_view(), name='annouceview'),
    path('classworkview/<int:id>/', WorkView.as_view(), name='classworkview'),
]
