from django.urls import path
from .views import (
    BusRouteCreateView, SchedulesDeleteView,
    SchedulesDetailView, SchedulesListView,
    SchedulesUpdateView
)


app_name = 'schedules'

urlpatterns = [
    path(
        'rotas/cadastrar/',
        BusRouteCreateView.as_view(),
        name='route_insert'
    ),
    path(
        'rotas/<int:id>/',
        SchedulesDetailView.as_view(),
        name='schedules_detail'
    ),
    path(
        'rotas/<int:int>/deletar/',
        SchedulesDeleteView.as_view(),
        name='schedules_delete'
    ),
    path(
        'rotas/',
        SchedulesListView.as_view(),
        name='schedules_list'
    ),
    path(
        'rotas/<int:id>/editar/',
        SchedulesUpdateView.as_view(),
        name='schedules_update'
    ),
]
