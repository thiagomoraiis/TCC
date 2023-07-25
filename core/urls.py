from django.urls import path
from .views import login, index

urlpatterns = [
    path('', index, name="login"),
    path('login/', login, name="login")
]