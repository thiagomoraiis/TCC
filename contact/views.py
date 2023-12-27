from django.views.generic import (
    ListView, CreateView,
    DeleteView, UpdateView,
    )
from .forms import ContactModelForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Contact
from django.urls import reverse_lazy


class ContactListView(ListView):
    template_name = 'contact/pages/contacts_list.html'
    queryset = Contact.objects.all().prefetch_related('posted_by')
    context_object_name = 'contact'
    paginate_by = 2

    def get_queryset(self):
        qs = super().get_queryset().order_by('sector')
        return qs


class ContactCreateView(UserPassesTestMixin, CreateView):
    template_name = 'contact/pages/contact_insert.html'
    form_class = ContactModelForm
    context_object_name = 'form'
    model = Contact
    login_url = '/users/accounts/login/'
    success_url = reverse_lazy('core:index')

    def test_func(self) -> bool | None:
        return self.request.user.is_superuser 

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


class ContactDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'contact/pages/contact_delete.html'
    model = Contact
    queryset = Contact.objects.all()
    context_object_name = 'contact'
    pk_url_kwarg = 'id'
    login_url = '/users/accounts/login/'
    success_url = reverse_lazy('contact:contact_list')

    def test_func(self) -> bool | None:
        return self.request.user.is_superuser 


class ContactUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'contact/pages/contact_insert.html'
    queryset = Contact.objects.all()
    context_object_name = 'contact'
    form_class = ContactModelForm
    pk_url_kwarg = 'id'
    login_url = '/users/accounts/login/'
    success_url = reverse_lazy('contact:contact_list')

    def test_func(self) -> bool | None:
        return self.request.user.is_superuser 
