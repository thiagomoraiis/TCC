from django.urls import path
from .views import (IndexListView, PresentationTemplateView,
                    simulator, about)

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
        'simulator/', simulator, name='simulator'
    ),
    # path('post/criar', create_post),
    path(
        'sobre/', about, name='about'
    )
]
