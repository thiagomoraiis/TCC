from django.views.generic import (
    ListView, CreateView, DetailView,
    DeleteView, UpdateView
)
from .models import BusRoute
from .forms import BusRouteModelForm
from django.urls import reverse_lazy


class BusRouteCreateView(CreateView):
    template_name = 'schedules/pages/schedules_insert.html'
    form_class = BusRouteModelForm
    model = BusRoute
    success_url = reverse_lazy('core:index')
    # context_object_name = 'form'

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        form.instance.destiny = 'Pau dos Ferros'
        return super().form_valid(form)


class SchedulesListView(ListView):
    template_name = 'schedules/pages/schedules_list.html'
    queryset = BusRoute.objects.all()
    context_object_name = 'schedules'

    def get_queryset(self):
        qs = super().get_queryset()
        qs.order_by('origin')

        city = self.request.GET.get('city')

        if city:
            qs = qs.filter(name__icontains=city)

        return qs


class SchedulesDeleteView(DeleteView):
    template_name = 'schedules/pages/schedules_delete.html'
    model = BusRoute
    queryset = BusRoute.objects.all()
    context_object_name = 'schedules'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('core:index')


class SchedulesDetailView(DetailView):
    template_name = 'schedules/pages/schedules_detail.html'
    model = BusRoute
    context_object_name = 'schedules'
    queryset = BusRoute.objects.all()
    pk_url_kwarg = 'id'


class SchedulesUpdateView(UpdateView):
    template_name = 'schedules/pages/schedules_insert.html'
    queryset = BusRoute.objects.all()
    context_object_name = 'schedules'
    form_class = BusRouteModelForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('schedules:schedules_list')
