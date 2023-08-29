from django.urls import path
from .views import list_city

app_name = 'city'

urlpatterns = [
    path('list/', list_city, name='list_city')
]
