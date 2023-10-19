from django.views.generic import (
    TemplateView, CreateView
    )
from .forms import CityModelForm
from .models import City
from django.urls import reverse_lazy


class CityListView(TemplateView):  # trocar para ListView
    template_name = 'city/pages/city_list.html'


class CityDetailView(TemplateView):  # trocar para DetailView
    template_name = 'city/pages/city_detail.html'


class CityCreateView(CreateView):
    template_name = 'city/pages/city_insert.html'
    form_class = CityModelForm
    context_object_name = 'form'
    model = City
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)
