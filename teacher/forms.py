from cProfile import label
from django.contrib.auth.models import User
from django import forms
from django.forms import fields, widgets
from django.core import validators
from django.utils.translation import gettext_lazy as _

from .models import CreateClass


class CreateClassForm(forms.ModelForm):
    class Meta:
        model = CreateClass
        fields = ('class_code_name', 'section',
                  'subject_name', 'room', 'classcode')

        labels = {"class_code_name": "Subject Code"}

        widgets = {
            'class_code_name': forms.TextInput(attrs={'placeholder': 'Class Code'}),
            'section': forms.TextInput(attrs={'placeholder': 'Section'}),
            'subject_name': forms.TextInput(attrs={'placeholder': 'Subject name'}),
            'room': forms.EmailInput(attrs={'placeholder': 'Room'}),
            'classcode': forms.PasswordInput(attrs={'placeholder': 'Code'}),

        }
