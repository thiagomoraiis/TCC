from django import forms


class EmailForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class', 'form-control d-block'}
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control d-block'}
    ))
    subject = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control d-block w-100'}
    ))
