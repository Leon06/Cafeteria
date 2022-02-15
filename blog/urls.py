from unicodedata import name
from urllib.parse import urlparse
from django.urls import path
from .views import Blog, category

app_name='blog'

urlpatterns = [
    path('',Blog.as_view(),name='blog'),
    path('category/<int:category_id>/',category, name="category")
]
