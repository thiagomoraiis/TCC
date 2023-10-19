from django.views.generic import (TemplateView, CreateView)
from .models import Tip
from .forms import TipsModelForm
from django.urls import reverse_lazy


class TipsCreateView(CreateView):
    template_name = 'tip/pages/tips_insert.html'
    form_class = TipsModelForm
    context_object_name = 'form'
    model = Tip
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


class TipsListView(TemplateView):
    template_name = 'tip/pages/tips_list.html'


class TipsDetailView(TemplateView):
    template_name = 'tip/pages/tips_detail.html'
