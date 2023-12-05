from .models import Tip
from .forms import TipsModelForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, CreateView, UpdateView,
    DeleteView, DetailView
)


class TipsCreateView(LoginRequiredMixin, CreateView):
    template_name = 'tip/pages/tips_insert.html'
    form_class = TipsModelForm
    context_object_name = 'form'
    model = Tip
    login_url = '/users/accounts/login/'
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


class TipsListView(ListView):
    template_name = 'tip/pages/tips_list.html'
    queryset = Tip.objects.all().prefetch_related('posted_by')
    context_object_name = 'tips'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        import re

        image_urls = []

        tips = self.get_queryset().order_by('-id')

        for tip in tips:
            content = tip.content

            matches = re.findall(r'<img .*?src="(.*?)".*?>', content)

            if matches:
                image_urls.extend(matches)

        context['image_urls'] = image_urls
        context['tips'] = tips
        return context


class TipsDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'tip/pages/tips_delete.html'
    model = Tip
    queryset = Tip.objects.all()
    context_object_name = 'tips'
    pk_url_kwarg = 'id'
    login_url = '/users/accounts/login/'
    success_url = reverse_lazy('core:index')


class TipsDetailView(DetailView):
    template_name = 'tip/pages/tips_detail.html'
    model = Tip
    context_object_name = 'tips'
    queryset = Tip.objects.all()
    pk_url_kwarg = 'id'


class TipsUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'tip/pages/tips_insert.html'
    queryset = Tip.objects.all()
    context_object_name = 'tips'
    form_class = TipsModelForm
    pk_url_kwarg = 'id'
    login_url = '/users/accounts/login/'
    success_url = reverse_lazy('tips:tips_list')
