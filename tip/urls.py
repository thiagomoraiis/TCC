from django.urls import path
from .views import TipsListView, TipsDetailView


app_name = 'tip'

urlpatterns = [
    path('', TipsListView.as_view(), name='tips_list'),
    path('detalhe-dicas/', TipsDetailView.as_view(), name='tips_detail'),
]
