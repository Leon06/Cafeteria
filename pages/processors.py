
from .models import Page

def cotext_processors(request):
    pages = Page.objects.all()
    ctx = {'pages': pages}
    return ctx
    

