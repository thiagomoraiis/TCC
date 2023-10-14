from django.shortcuts import render


def login(request):
    return render(request, 'user/pages/login_form.html')


def register(request):
    return render(request, 'user/pages/register_form.html')
