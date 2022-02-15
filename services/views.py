
from django.shortcuts import render

from django.views.generic import TemplateView
from .models import Service as ServiceModel

class Services(TemplateView):
    template_name = 'services/services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = ServiceModel.objects.all()
        return context


