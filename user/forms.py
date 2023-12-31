from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from django.core.exceptions import ValidationError


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'user', 'age', 'is_student', 'city',
            'bio', 'photo'
        ]
        widgets = {
            'age': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'is_student': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
            ),
            'city': forms.Select(
                attrs={'class': 'form-control selectric'}
            ),
            'bio': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'photo': forms.FileField(),
        }


class UserModelForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name',
            'email',
            'password1', 'password2'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))
