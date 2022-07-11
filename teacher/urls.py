from django.urls import path
from .views import TeacherHome, CreateClassview, ClassShow, userlogout, deletecard, deletelist, Addworkview, ShowWorkview, deletework, PasswordChangeView, UpdateAccountView, pdf_view, EditworkView, EditAnnouceView, ExamView
urlpatterns = [
    path('', TeacherHome.as_view(), name='home'),
    path('create', CreateClassview.as_view(), name='create'),
    path('classshow/<int:id>/', ClassShow.as_view(), name='classshow'),
    path('addwork/<int:id>/', Addworkview.as_view(), name='addwork'),
    path('showmywork/<int:id>/', ShowWorkview.as_view(), name='showmywork'),
    path('editwork/<int:id>/', EditworkView.as_view(), name='editwork'),
    path('editlist/<int:id>/', EditAnnouceView.as_view(), name='editlist'),
    path('change_password', PasswordChangeView.as_view(), name='change_password'),
    path('update_account', UpdateAccountView.as_view(), name='update_account'),
    path('examview/<int:id>/', ExamView.as_view(), name='examview'),
    path('userlogout', userlogout, name='userlogout'),
    path('deletecard/<int:id>/', deletecard, name='deletecard'),
    path('deletelist/<int:id>/', deletelist, name='deletelist'),
    path('deletework/<int:id>/', deletework, name='deletework'),
    path('pdf_view/<int:id>', pdf_view, name='pdf_view'),
]
