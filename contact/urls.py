from django.urls import path
from .views import (
    ContactListView, ContactCreateView,
    ContactDeleteView, ContactUpdateView
)

app_name = 'contact'

urlpatterns = [
    path(
        '',
        ContactListView.as_view(),
        name='contact_list'
    ),
    path(
        'cadastrar/',
        ContactCreateView.as_view(),
        name='contact_insert'
    ),
    path(
        '<int:id>/deletar/',
        ContactDeleteView.as_view(),
        name='contact_delete',
    ),
    path(
        '<int:id>/atualizar/',
        ContactUpdateView.as_view(),
        name='contact_update',
    )
]
