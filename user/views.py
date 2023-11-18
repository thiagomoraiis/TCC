from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserModelForm, LoginForm
from django.contrib.auth import login, logout, authenticate


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'user/pages/login_form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user:
                login(self.request, user)
                return redirect('core:index')

        return render(request, 'user/pages/login_form.html', {'form': form})


class RegisterView(View):
    def get(self, request):
        form = UserModelForm()
        return render(request, 'user/pages/register_form.html', {'form': form})

    def post(self, request):
        form = UserModelForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.is_active = True
            user.is_staff = True
            user.save()
            return redirect('user:login')

        return render(request, 'user/pages/register_form.html', {'form': form})


def logout_(request):
    logout(request)
    return redirect('user:login')
