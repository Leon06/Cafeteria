from django.urls import path
from .views import Services

app_name = 'services'

urlpatterns = [
    path('',Services.as_view(),name='services')
]
