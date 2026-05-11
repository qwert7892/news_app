from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *
from django.db import models
from django.forms import ModelForm


class UserCreationCustomForm(UserCreationForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Почта', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'type': "password"}))
    password2 = forms.CharField(label='Подтвердите пароль',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'type': "password"}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'type': "password"}))


class NewsCreationForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'summary', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'summary': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class NewsForm(forms.Form):
    title = forms.CharField(
        min_length=0,
        max_length=100,
        label="Заголовок",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }))

    summary = forms.CharField(
        max_length=200,
        label="Краткое описание",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }))

    content = forms.CharField(label="Текст новости", widget=forms.Textarea(attrs={
        'class': 'form-control',
    }))

    photo = forms.ImageField(
        label="Обложка",
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': 'image/*',
        })
    )
