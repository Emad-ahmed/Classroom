from cProfile import label
from urllib import request
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
            'class_code_name': forms.TextInput(attrs={'placeholder': 'Subject Code'}),
            'section': forms.TextInput(attrs={'placeholder': 'Section'}),
            'subject_name': forms.TextInput(attrs={'placeholder': 'Subject name'}),
            'room': forms.TextInput(attrs={'placeholder': 'Room'}),
            'classcode': forms.TextInput(attrs={'placeholder': 'Code'}),
        }

    def clean_classcode(self):
        classcode = self.cleaned_data['classcode']
        if CreateClass.objects.filter(classcode=classcode).exists():
            raise forms.ValidationError("Class Code Already Exists")

        return classcode

    def clean_class_code_name(self):
        class_code_name = self.cleaned_data['class_code_name']
        if (CreateClass.objects.filter(class_code_name=class_code_name).exists()) and (CreateClass.objects.filter(user=request.user).exists()):
            raise forms.ValidationError("Subject Code Already Exitst")

        return class_code_name
