from django.urls import path
from .views import (
    ContactListView, ContactCreateView
)

app_name = 'contacts'

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
    )
]
