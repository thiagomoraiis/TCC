from django.shortcuts import render


def city_list(request):
    return render(request, 'city/pages/city_list.html')


def city_detail(request):
    return render(request, 'city/pages/city_detail.html')
