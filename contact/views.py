from django.shortcuts import render


def list_contacts(request):
    return render(request, 'contact/pages/list_contacts.html')
