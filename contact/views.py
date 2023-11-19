from django.views.generic import (
    ListView, CreateView
    )
from .forms import ContactModelForm
from .models import Contact
from django.urls import reverse_lazy


class ContactListView(ListView):
    template_name = 'contact/pages/contacts_list.html'
    queryset = Contact.objects.all()
    context_object_name = 'contact'


class ContactCreateView(CreateView):
    template_name = 'contact/pages/contact_insert.html'
    form_class = ContactModelForm
    context_object_name = 'form'
    model = Contact
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)
