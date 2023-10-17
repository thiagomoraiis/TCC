from django.urls import path
from .views import EventCreateView

app_name = 'event'

urlpatterns = [
    path('cadastrar/', EventCreateView.as_view(), name='')
]
