from django.shortcuts import render
from django.views.generic import View


class LoginView(View):
    def get(self, request):
        return render(request, 'user/pages/login_form.html')

    def post(self, request):
        return render(request, 'user/pages/login_form.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'user/pages/register_form.html')

    def post(self, request):
        return render(request, 'user/pages/register_form.html')
