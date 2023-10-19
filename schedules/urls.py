from django.urls import path
from .views import BusRouteCreateView


app_name = 'schedules'

urlpatterns = [
    path('rotas/', BusRouteCreateView.as_view(), name='route-insert'),
    # path('rotas/', BusRouteCreateView.as_view(), name='route-list'),
]
