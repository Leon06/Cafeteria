from django.urls import path
from .views import Home,About,Store

app_name="cafeteria"

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('about/',About.as_view(),name='about'),
    path('store/',Store.as_view(),name='store')
]
