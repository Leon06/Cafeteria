from .models import Link

def diccionario_contexto(request):
    context = {}
    links = Link.objects.all()
    for link in links:
        context[link.key] = link.url
    return context