from django.urls import path
from .views import tips_list, tips_detail


app_name = 'tip'

urlpatterns = [
    path('', tips_list, name='tips_list'),
    path('detalhe-dicas/', tips_detail, name='tips_detail'),
]
