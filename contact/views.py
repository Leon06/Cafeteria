import imp
from django.shortcuts import render
from django.views.generic import TemplateView

class Contact(TemplateView):
    template_name = 'contact/contact.html'
