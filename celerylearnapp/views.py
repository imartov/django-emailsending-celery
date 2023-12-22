from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .models import Contact
from .forms import ContactForm
from django.views.generic import CreateView
from .service import send
from .tasks import send_spam_email


class ContactView(CreateView):
    def get_success_url(self):
        return reverse('contact')

    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'

    def form_valid(self, form) -> HttpResponse:
        form.save()
        # send(form.instance.email)
        send_spam_email.delay(form.instance.email)
        return super().form_valid(form)


