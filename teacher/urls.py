from django.urls import path
from .views import TeacherHome, CreateClassview, ClassShow, userlogout, deletecard, deletelist
urlpatterns = [
    path('', TeacherHome.as_view(), name='home'),
    path('create', CreateClassview.as_view(), name='create'),
    path('classshow/<int:id>/', ClassShow.as_view(), name='classshow'),
    path('userlogout', userlogout, name='userlogout'),
    path('deletecard/<int:id>/', deletecard, name='deletecard'),
    path('deletelist/<int:id>/', deletelist, name='deletelist'),
]
