from django.urls import path
from .views import CityDetailView, CityListView, CityCreateView

app_name = 'city'

urlpatterns = [
    path('', CityListView.as_view(), name='city_list'),
    path('detalhe-cidade/', CityDetailView.as_view(), name='city_detail'),
    path('cadastrar/', CityCreateView.as_view(), name='city_insert'),
]
