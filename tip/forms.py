from django import forms
from .models import Tip


class TipsModelForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = [
            'title', 'description', 'content',
            'category', 'posted_by',
            'posted_at', 'updated_at', 'tip_about',
        ]
