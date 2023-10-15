from django.views.generic import TemplateView


class CityListView(TemplateView):  # trocar para ListView
    template_name = 'city/pages/city_list.html'


class CityDetailView(TemplateView):  # trocar para DetailView
    template_name = 'city/pages/city_detail.html'
