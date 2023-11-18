from django import forms
from .models import Tip
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class TipsModelForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), required=False)

    class Meta:
        model = Tip
        fields = [
            'title', 'description', 'content',
            'category', 'tip_about',
        ]
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'description': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'category': forms.Select(
                attrs={'class': 'form-control selectric'}
            ),
            'content': CKEditorUploadingWidget(),
            'tip_about': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
        }
