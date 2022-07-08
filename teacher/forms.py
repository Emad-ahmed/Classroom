from cProfile import label
from urllib import request
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django import forms
from django.forms import fields, widgets
from django.core import validators
from django.utils.translation import gettext_lazy as _

from .models import CreateClass, AddClassWork


class UpdateSignForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username',  'first_name', 'last_name', 'email')

        labels = {'email': "Email"}

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email Already Exists")

        return email


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
        fields = ('mytopic', 'description', 'marks', 'imagephoto',
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


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'autofocus': True, 'class': 'form-control', 'placeholder': 'Old Password'}))
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'New Password'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'Confirm New Password'}))
