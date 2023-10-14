from django.urls import path
from .views import city_list, city_detail

app_name = 'city'

urlpatterns = [
    path('', city_list, name='city_list'),
    path('detalhe-cidade/', city_detail, name='city_detail')
]
