from django.urls import path
from .views import list_city, detalhe_cidade

app_name = 'city'

urlpatterns = [
    path('list/', list_city, name='list_city'),
    path('detalhe-cidade/', detalhe_cidade, name='detalhe-cidade')
]
