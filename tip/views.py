from django.views.generic import TemplateView


class TipsListView(TemplateView):
    template_name = 'tip/pages/tips_list.html'


class TipsDetailView(TemplateView):
    template_name = 'tip/pages/tips_detail.html'
