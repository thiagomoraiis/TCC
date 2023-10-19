from django.urls import path
from .views import (
    IndexListView, PresentationTemplateView, SimulatorTemplateView,
    AboutTemplateView, CreatePost)

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
        'post/criar', CreatePost.as_view(), name='create-post'
    ),
    path(
        'sobre/', AboutTemplateView.as_view(), name='about'
    )
]
