from django.urls import path
from .views import ContactListView

app_name = 'contacts'

urlpatterns = [
    path('list/', ContactListView.as_view(), name='contact_list'),
]
