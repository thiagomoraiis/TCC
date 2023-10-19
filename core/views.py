from django.views.generic import (TemplateView, CreateView)
from tip.forms import TipsModelForm
from django.urls import reverse_lazy
from tip.models import Tip


class IndexListView(TemplateView):  # trocar para ListView
    template_name = 'core/pages/index.html'


class PresentationTemplateView(TemplateView):
    template_name = 'core/pages/presentation.html'


class SimulatorTemplateView(TemplateView):
    template_name = 'core/pages/simulator.html'


class AboutTemplateView(TemplateView):
    template_name = 'core/pages/about.html'


class CreatePost(CreateView):
    template_name = 'core/pages/create_post.html'
    form_class = TipsModelForm
    context_object_name = 'form'
    model = Tip
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


class DetailPost(TemplateView):
    template_name = 'core/pages/detail_news.html'
