from django.views.generic import (
    ListView, CreateView, DetailView,
    DeleteView, UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BusRoute
from .forms import BusRouteModelForm
from django.urls import reverse_lazy


class BusRouteCreateView(LoginRequiredMixin, CreateView):
    template_name = 'schedules/pages/schedules_insert.html'
    form_class = BusRouteModelForm
    model = BusRoute
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        form.instance.destiny = 'Pau dos Ferros'
        return super().form_valid(form)


class SchedulesListView(ListView):
    template_name = 'schedules/pages/schedules_list.html'
    queryset = BusRoute.objects.all().prefetch_related('origin', 'posted_by')
    context_object_name = 'schedules'
    paginate_by = 1

    def get_queryset(self):
        qs = super().get_queryset()
        qs.order_by('origin')

        city = self.request.GET.get('city')

        if city:
            qs = qs.filter(name__icontains=city)

        return qs


class SchedulesDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'schedules/pages/schedules_delete.html'
    model = BusRoute
    queryset = BusRoute.objects.all()
    context_object_name = 'schedules'
    pk_url_kwarg = 'id'
    login_url = '/users/accounts/login/'
    success_url = reverse_lazy('core:index')


class SchedulesDetailView(DetailView):
    template_name = 'schedules/pages/schedules_detail.html'
    model = BusRoute
    context_object_name = 'schedules'
    queryset = BusRoute.objects.all()
    login_url = '/users/accounts/login/'
    pk_url_kwarg = 'id'


class SchedulesUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'schedules/pages/schedules_insert.html'
    queryset = BusRoute.objects.all()
    context_object_name = 'schedules'
    form_class = BusRouteModelForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('schedules:schedules_list')
