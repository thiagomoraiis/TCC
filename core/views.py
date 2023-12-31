from typing import Any
from tip.forms import TipsModelForm
from django.shortcuts import render
from django.urls import reverse_lazy
from tip.models import Tip
from event.models import Event
from .forms import EmailForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.views.generic import (
    TemplateView, CreateView, ListView, View
    # DetailView
)


class IndexListView(ListView):
    template_name = 'core/pages/index.html'
    model = Event
    queryset = Event.objects.all().prefetch_related('posted_by')[:3]

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


class PresentationTemplateView(View):
    template_name = 'core/pages/presentation.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request):
        form = EmailForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data.get('subject', '')
            message = form.cleaned_data.get('message', '')
            email = form.cleaned_data.get('email', '')

            admin_email = 'thiagomorais2605@gmail.com'

            send_mail(
                subject,
                f'Mensagem para {email}:\n\n{message}',
                email,
                [admin_email],
                fail_silently=False,
            )

            return HttpResponseRedirect('/')
        
        return self.render_to_response({'form': form})


class SimulatorTemplateView(TemplateView):
    template_name = 'core/pages/simulator.html'


class AboutTemplateView(TemplateView):
    template_name = 'core/pages/about.html'

def error404(request, exception):
    return render(request, 'core/pages/error404.html', status=404)


def error500(request):
    return render(request, 'core/pages/error500.html', status=500)
