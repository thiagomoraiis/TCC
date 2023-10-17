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
        'presentation', PresentationTemplateView.as_view(), name='presentation'
    ),
    # path('post/detalhe/', detail_news, name="detail"),
    path(
        'simulator/', SimulatorTemplateView.as_view(), name='simulator'
    ),
    path('post/criar', CreatePost.as_view(), name='create-post'),
    path(
        'sobre/', AboutTemplateView.as_view(), name='about'
    )
]
