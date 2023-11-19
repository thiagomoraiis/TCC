from django.urls import path
from .views import EventCreateView, EventDetailView


app_name = 'event'

urlpatterns = [
    path('cadastrar/', EventCreateView.as_view(), name='event_insert'),
    path('detalhe/<int:id>/', EventDetailView.as_view(), name='event_detail'),
]
