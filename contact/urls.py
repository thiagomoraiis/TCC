from django.urls import path
from .views import list_contacts

app_name = 'schedules'

urlpatterns = [
    path('list/', list_contacts, name='list_contacts'),
]
