from django.views.generic import (
    ListView, CreateView,
    DeleteView, UpdateView,
    )
from .forms import ContactModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Contact
from django.urls import reverse_lazy


class ContactListView(ListView):
    template_name = 'contact/pages/contacts_list.html'
    queryset = Contact.objects.all()
    context_object_name = 'contact'


class ContactCreateView(LoginRequiredMixin, CreateView):
    template_name = 'contact/pages/contact_insert.html'
    form_class = ContactModelForm
    context_object_name = 'form'
    model = Contact
    login_url = '/users/accounts/login/'
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


class ContactDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'contact/pages/contact_delete.html'
    model = Contact
    queryset = Contact.objects.all()
    context_object_name = 'contact'
    pk_url_kwarg = 'id'
    login_url = '/users/accounts/login/'
    success_url = reverse_lazy('contact:contact_list')


class ContactUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'contact/pages/contact_insert.html'
    queryset = Contact.objects.all()
    context_object_name = 'contact'
    form_class = ContactModelForm
    pk_url_kwarg = 'id'
    login_url = '/users/accounts/login/'
    success_url = reverse_lazy('contact:contact_list')
