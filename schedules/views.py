from django.views.generic import (TemplateView, CreateView)
from .models import BusRoute
from .forms import BusRouteModelForm
from django.urls import reverse_lazy


class BusRouteCreateView(CreateView):
    template_name = 'schedules/pages/schedules_insert.html'
    form_class = BusRouteModelForm
    context_object_name = 'form'
    model = BusRoute
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


class ScheduleListView(TemplateView):
    template_name = ''


class ScheduleDetailView(TemplateView):
    template_name = ''
