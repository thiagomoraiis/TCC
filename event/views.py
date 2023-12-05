from django.shortcuts import render # noqa
from django.views.generic import (
    CreateView, ListView, DeleteView, DetailView, UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import EventModelForm
from .models import Event
from django.urls import reverse_lazy


class EventListView(ListView):
    template_name = 'event/pages/events_list.html'
    queryset = Event.objects.all().prefetch_related('posted_by')
    context_object_name = 'event'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset().order_by('-id')
        return qs


class EventCreateView(LoginRequiredMixin, CreateView):
    template_name = 'event/pages/event_insert.html'
    form_class = EventModelForm
    context_object_name = 'form'
    model = Event
    login_url = '/users/accounts/login/'
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


class EventDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'event/pages/event_delete.html'
    model = Event
    queryset = Event.objects.all()
    context_object_name = 'event'
    pk_url_kwarg = 'id'
    login_url = '/users/accounts/login/'
    success_url = reverse_lazy('core:index')


class EventDetailView(DetailView):
    template_name = 'event/pages/event_detail.html'
    model = Event
    context_object_name = 'event'
    queryset = Event.objects.all()
    pk_url_kwarg = 'id'


class EventUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'event/pages/event_insert.html'
    queryset = Event.objects.all()
    context_object_name = 'event'
    form_class = EventModelForm
    pk_url_kwarg = 'id'
    login_url = '/users/accounts/login/'
    success_url = reverse_lazy('core:index')
