from django.urls import path
from .views import (
    CityDetailView, CityListView,
    CityCreateView, CityDeleteView,
    CityUpdateView
    )


app_name = 'city'

urlpatterns = [
    path(
        '',
        CityListView.as_view(),
        name='city_list'
    ),
    path(
        'detalhe-cidade/<int:id>/',
        CityDetailView.as_view(),
        name='city_detail'
    ),
    path(
        'cadastrar/',
        CityCreateView.as_view(),
        name='city_insert'
    ),
    path(
        'deletar/<int:id>/',
        CityDeleteView.as_view(),
        name='city_delete'
    ),
    path(
        'detalhe-cidade/<int:id>/editar/',
        CityUpdateView.as_view(),
        name='city_update'
    ),
]
