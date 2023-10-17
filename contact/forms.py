from django import forms
from .models import Contact


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'sector', 'telephone', 'coordinator',
            'email', 'posted_by'
        ]
        widgets = {
            'sector': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'coordinator': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }
