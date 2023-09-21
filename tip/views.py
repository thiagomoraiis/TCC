from django.shortcuts import render


def list_dicas(request):
    return render(request, 'tip/pages/list_dicas.html')


def detalhe_dicas(request):
    return render(request, 'tip/pages/detalhe_dicas.html')
