from django.urls import path
from .views import (
    IndexListView, PresentationTemplateView, SimulatorTemplateView,
    AboutTemplateView)

app_name = 'core'

urlpatterns = [
    path(
        '', IndexListView.as_view(), name='index'
    ),
    path(
        'apresentacao', PresentationTemplateView.as_view(), name='presentation'
    ),
    path(
        'simulador/', SimulatorTemplateView.as_view(), name='simulator'
    ),
    path(
        'sobre/', AboutTemplateView.as_view(), name='about'
    )
]
