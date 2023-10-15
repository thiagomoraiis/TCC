from django.views.generic import TemplateView


class IndexListView(TemplateView):  # trocar para ListView
    template_name = 'core/pages/index.html'


class PresentationTemplateView(TemplateView):
    template_name = 'core/pages/presentation.html'


class SimulatorTemplateView(TemplateView):
    template_name = 'core/pages/simulator.html'


class AboutTemplateView(TemplateView):
    template_name = 'core/pages/about.html'


class CreatePost(TemplateView):
    template_name = 'core/pages/create_post.html'


class DetailPost(TemplateView):
    template_name = 'core/pages/detail_news.html'
