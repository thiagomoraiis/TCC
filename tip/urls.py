from django.urls import path
from .views import TipsListView, TipsDetailView, TipsCreateView


app_name = 'tip'

urlpatterns = [
    path('', TipsListView.as_view(), name='tips-list'),
    path('detalhe-dicas/', TipsDetailView.as_view(), name='tips-detail'),
    path('cadastrar/', TipsCreateView.as_view(), name='tips-insert'),
]
