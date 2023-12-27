from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserModelForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'user/pages/login_form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user and user.is_active:
                login(request, user)

                next_url = request.GET.get('next', 'core:index')
                return redirect(next_url)
            else:
                messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')

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
            user.save()
            return redirect('user:login')

        return render(request, 'user/pages/register_form.html', {'form': form})


def logout_(request):
    logout(request)
    return redirect('user:login')
