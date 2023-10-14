from django.shortcuts import render


def contact_list(request):
    return render(request, 'contact/pages/contacts_list.html')
