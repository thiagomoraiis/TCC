from django.shortcuts import render


def index(request):
    return render(request, 'core/pages/index.html')