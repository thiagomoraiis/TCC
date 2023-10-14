from django.shortcuts import render


def tips_list(request):
    return render(request, 'tip/pages/tips_list.html')


def tips_detail(request):
    return render(request, 'tip/pages/tips_detail.html')
