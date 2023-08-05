from django.urls import path
from .views import login, index, presentation, detail_news, register, simulator

app_name = 'core'

urlpatterns = [
    path('', index, name="index"),
    path('presentation', presentation, name='presentation'),
    path('login/', login, name="login"),
    path('detail/', detail_news, name="detail"),
    path('register/', register, name="register"),
    path('simulator/', simulator, name="simulator"),
]
