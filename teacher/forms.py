from cProfile import label
from urllib import request
from django.contrib.auth.models import User
from django import forms
from django.forms import fields, widgets
from django.core import validators
from django.utils.translation import gettext_lazy as _

from .models import CreateClass, AddClassWork


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


class AddClassWorkForm(forms.ModelForm):
    class Meta:
        model = AddClassWork
        fields = ('mytopic', 'description', 'imagephoto',
                  'document', 'end_date_time')
        labels = {"mytopic": "Topic",
                  "description": "Description", 'imagephoto': "image"}
        widgets = {
            'mytopic': forms.Select(attrs={'placeholder': 'Topic'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'imagephoto': forms.FileInput(attrs={'placeholder': 'Image'}),
            'document': forms.FileInput(attrs={'placeholder': 'Document'}),
            'end_date_time': forms.DateTimeInput(attrs={'placeholder': 'Y-m-d H:M:S', 'type': 'datetime-local'}),
        }
