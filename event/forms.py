from django import forms
from .models import Event
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class EventModelForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title', 'description', 'content',
            'category', 'posted_by', 'date', 'local'
        ]
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'description': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'content': CKEditorUploadingWidget(),
            'category': forms.Select(
                attrs={'class': 'form-control selectric'}
            ),
            'date': forms.DateInput(
                attrs={'class': 'form-control'}
            ),
            'local': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
        }
