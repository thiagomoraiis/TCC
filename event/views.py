from django.shortcuts import render # noqa
from django.views.generic import CreateView, TemplateView
from .forms import EventModelForm
from .models import Event
from django.urls import reverse_lazy


class EventCreateView(CreateView):
    template_name = 'event/pages/event_insert.html'
    form_class = EventModelForm
    context_object_name = 'form'
    model = Event
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


class EventDetailView(TemplateView):
    template_name = 'event/pages/event_detail.html'