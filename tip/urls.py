from django.urls import path
from .views import list_dicas, detalhe_dicas

app_name = 'tip'

urlpatterns = [
    path('', list_dicas, name='list_dicas'),
    path('detalhe-dicas/', detalhe_dicas, name='detalhe-dicas'),
]
