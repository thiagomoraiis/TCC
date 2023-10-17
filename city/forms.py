from django import forms
from .models import City


class CityModelForm(forms.ModelForm):
    class Meta:
        model = City
        fields = [
            'name', 'bus_dispo', 'posted_by'
        ]
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'bus_dispo': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
            ),
        }
