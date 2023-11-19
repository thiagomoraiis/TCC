from typing import Any
from tip.forms import TipsModelForm
from django.urls import reverse_lazy
from tip.models import Tip
from event.models import Event
from django.views.generic import (
    TemplateView, CreateView, ListView,
    # DetailView
)


class IndexListView(ListView):
    template_name = 'core/pages/index.html'
    model = Event
    # context_object_name = 'event'
    queryset = Event.objects.all()

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        import re

        image_urls = []

        posts = self.get_queryset()

        for post in posts:
            content = post.content

            matches = re.findall(r'<img .*?src="(.*?)".*?>', content)

            if matches:
                image_urls.extend(matches)

        context['image_urls'] = image_urls
        context['event'] = posts
        return context


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


# class DetailPost(DetailView):
#     template_name = 'core/pages/detail_news.html'
#     queryset = Event.objects.all()[:4]
#     context_object_name = 'event'
#     pk_url_kwarg = 'id'
