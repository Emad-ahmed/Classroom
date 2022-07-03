from django.urls import path
from .views import StudentHome
urlpatterns = [
    path('', StudentHome.as_view(), name='home')

]
