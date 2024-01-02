from typing import Any
from django.shortcuts import render
from event.models import Event
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.views.generic import (
    TemplateView, CreateView, ListView, View
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


@method_decorator(login_required, name='dispatch')
class PresentationTemplateView(View):
    template_name = 'core/pages/presentation.html'

    @method_decorator(login_required, name='post')
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        subject = self.request.POST.get('subject')
        message = self.request.POST.get('message')
        email = self.request.POST.get('email')
        admin_email = 't.morais@escolar.ifrn.edu.br'

        try:
            send_mail(
                subject,
                message,
                email,
                [admin_email],
                fail_silently=False,
            )
            messages.success(request, 'E-mail enviado com sucesso!')
            return HttpResponseRedirect('/')

        except Exception as e:
            messages.error(request, 'Erro ao enviar o formulário')
            return HttpResponseRedirect('/apresentacao')


class SimulatorTemplateView(TemplateView):
    template_name = 'core/pages/simulator.html'


class AboutTemplateView(TemplateView):
    template_name = 'core/pages/about.html'

def error404(request, exception):
    return render(request, 'core/pages/error404.html', status=404)


def error500(request):
    return render(request, 'core/pages/error500.html', status=500)
