from django.urls import path
from .views import LoginView, RegisterView, logout_


app_name = 'user'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_, name='logout')
]
