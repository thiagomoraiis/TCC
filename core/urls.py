from django.urls import path
from .views import login, index, presentation

app_name = 'core'

urlpatterns = [
    path('', index, name="index"),
    path('presentation', presentation, name='presentation'),
    path('login/', login, name="login")
]