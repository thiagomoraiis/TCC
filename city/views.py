from .forms import CityModelForm
from .models import City
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView, ListView, DetailView, DeleteView, UpdateView
)


class CityListView(ListView):
    template_name = 'city/pages/city_list.html'
    queryset = City.objects.all().prefetch_related('posted_by')
    context_object_name = 'city'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        qs.order_by('name')

        city = self.request.GET.get('city')

        if city:
            qs = qs.filter(name__icontains=city)

        return qs


class CityDetailView(DetailView):
    template_name = 'city/pages/city_detail.html'
    model = City
    context_object_name = 'city'
    queryset = City.objects.all()
    pk_url_kwarg = 'id'


class CityCreateView(LoginRequiredMixin, CreateView):
    template_name = 'city/pages/city_insert.html'
    form_class = CityModelForm
    model = City
    login_url = '/users/accounts/login/'
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


class CityDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'city/pages/city_delete.html'
    model = City
    queryset = City.objects.all()
    context_object_name = 'city'
    pk_url_kwarg = 'id'
    login_url = '/users/accounts/login/'
    success_url = reverse_lazy('city:city_list')


class CityUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'city/pages/city_insert.html'
    queryset = City.objects.all()
    context_object_name = 'city'
    form_class = CityModelForm
    pk_url_kwarg = 'id'
    login_url = '/users/accounts/login/'
    success_url = reverse_lazy('city:city_list')
