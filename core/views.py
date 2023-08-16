from django.shortcuts import render


def index(request):
    return render(request, 'core/pages/index.html')


def presentation(request):
    return render(request, 'core/pages/presentation.html')


def login(request):
    return render(request, 'student/pages/form_login.html')


def detail_news(request):
    return render(request, 'core/pages/detail_news.html')


def register(request):
    return render(request, 'student/pages/form_register.html')


def simulator(request):
    return render(request, 'core/pages/simulator.html')


def create_post(request):
    return render(request, 'core/pages/create_post.html')
