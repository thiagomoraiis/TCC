from django import forms
from .models import Event


class EventModelForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title', 'description', 'content',
            'category', 'posted_by', 'posted_at',
            'updated_at', 'date', 'local'
        ]
