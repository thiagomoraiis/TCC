from django.views.generic import TemplateView


class ContactListView(TemplateView):
    template_name = 'contact/pages/contacts_list.html'
