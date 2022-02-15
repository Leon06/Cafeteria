
from django.shortcuts import render,get_object_or_404
from .models import Page

def page(request, page_id, page_slug):
    pages = get_object_or_404(Page, id=page_id)
    return render(request,'pages/sample.html', {'page':pages})




