from django.urls import path
from .views import (
    TipsListView, TipsDetailView, TipsCreateView,
    TipsDeleteView, TipsUpdateView
)


app_name = 'tips'

urlpatterns = [
    path(
        '',
        TipsListView.as_view(),
        name='tips_list'
    ),
    path(
        '<int:id>/',
        TipsDetailView.as_view(),
        name='tips_detail'
    ),
    path(
        'cadastrar/',
        TipsCreateView.as_view(),
        name='tips_insert'
    ),
    path(
        '<int:id>/editar/',
        TipsUpdateView.as_view(),
        name='tips_update'
    ),
    path(
        '<int:id>/deletar/',
        TipsDeleteView.as_view(),
        name='tips_delete'
    ),
]
