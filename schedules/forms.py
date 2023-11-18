from django import forms
from .models import BusRoute


class BusRouteModelForm(forms.ModelForm):
    class Meta:
        model = BusRoute
        fields = [
            'origin', 'shift',
            # 'destiny', 
            'arrival_time', 'departure_time',
        ]
        widgets = {
            'origin': forms.Select(attrs={'class': 'form-control selectric'}),
            # 'destiny': forms.Select(attrs={'class': 'form-control selectric'}),
            'shift': forms.Select(attrs={'class': 'form-control selectric'}),
            'arrival_time': forms.TextInput(attrs={'class': 'form-control'}),
            'departure_time': forms.TextInput(attrs={'class': 'form-control'}),
        }
