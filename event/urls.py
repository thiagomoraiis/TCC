from django.urls import path
from .views import (
    EventCreateView, EventDetailView,
    EventDeleteView, EventUpdateView
)


app_name = 'event'

urlpatterns = [
    path(
        'cadastrar/', EventCreateView.as_view(), name='event_insert'
    ),
    path(
        'detalhe/<int:id>/', EventDetailView.as_view(), name='event_detail'
    ),
    path(
        'deletar/<int:id>/', EventDeleteView.as_view(), name='event_delete'
    ),
    path(
        'editar/<int:id>/', EventUpdateView.as_view(), name='event_update'
    ),
]
