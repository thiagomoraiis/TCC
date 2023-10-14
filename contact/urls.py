from django.urls import path
from .views import contact_list

app_name = 'contacts'

urlpatterns = [
    path('list/', contact_list, name='contact_list'),
]
