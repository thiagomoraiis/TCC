from django import forms
from .models import BusRoute


class BusRouteModelForm(forms.ModelForm):
    class Meta:
        model = BusRoute
        fields = [
            'origin', 'destiny', 'shift',
            'arrival_time', 'departure_time',
            'posted_by',
        ]
        widgets = {
            'origin': forms.Select(attrs={'class': 'form-control selectric'}),
            'destiny': forms.Select(attrs={'class': 'form-control selectric'}),
            'shift': forms.TextInput(attrs={'class': 'form-control'}),
            'arrival_time': forms.TextInput(attrs={'class': 'form-control'}),
            'departure_time': forms.TextInput(attrs={'class': 'form-control'}),
        }
