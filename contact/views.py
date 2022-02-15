
from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

def contact(request):
    contact_form = ContactForm
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Enviamos el correo y direccionamos
            email = EmailMessage(
                "La Cafeteria: Nuevo mensaje de contacto",
                f'De: {name}\nEmail de Contacto: {email}\nMensaje: {content}',
                "no-contestar@inbox.com",
                ["leondiego66@yahoo.com"],
                reply_to=[email]
            )
            try:
                email.send()
                # Todo salio bien
                return redirect(reverse('contact:contact')+"?Ok")
            except:
                # ALgo salio mal
                return redirect(reverse('contact:contact')+"?fail")
    return render(request,'contact/contact.html',{'form':contact_form})


