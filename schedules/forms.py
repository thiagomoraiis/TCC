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
