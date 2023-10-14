from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'user', 'age', 'is_student', 'city',
            'bio', 'photo'
        ]


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name',
            'email', 'password'
        ]

        def __init__(self):
            for field, field_name in self.fields.values():
                field.widget.attrs['class'] = 'form-control'

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))

    def clean(self):
        cleaned_data = super().clean()
        self.passwords_equals_validator(cleaned_data)
        return cleaned_data

    def passwords_equals_validator(value):
        password = value.get('password')
        password1 = value.get('password')
        if password != password1:
            return ValidationError('As senhas não são iguais')


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))
