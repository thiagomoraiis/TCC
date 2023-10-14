from django.urls import path
from .views import (index, presentation,
                    simulator, about)

app_name = 'core'

urlpatterns = [
    path('', index, name="index"),
    path('presentation', presentation, name='presentation'),
    # path('post/detalhe/', detail_news, name="detail"),
    path('simulator/', simulator, name="simulator"),
    # path('post/criar', create_post),
    path('sobre/', about, name='about')
]
