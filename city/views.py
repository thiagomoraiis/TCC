from django.shortcuts import render


def list_city(request):
    return render(request, 'city/pages/list_city.html')
