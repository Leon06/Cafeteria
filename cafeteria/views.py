
from django.shortcuts import render
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'cafeteria/home.html'

class About(TemplateView):
    template_name = 'cafeteria/about.html'

class Store(TemplateView):
    template_name = 'cafeteria/store.html'


