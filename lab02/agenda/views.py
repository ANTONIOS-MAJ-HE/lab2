# agenda/views.py

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Contacto
from .forms import ContactoForm

def lista_contactos(request):
    contactos = Contacto.objects.all()
    return render(request, 'agenda/lista_contactos.html', {'contactos': contactos})

def crear_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactoForm()
    return render(request, 'agenda/crear_contacto.html', {'form': form})

def editar_contacto(request, contacto_id):
    contacto = Contacto.objects.get(id=contacto_id)
    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactoForm(instance=contacto)
    return render(request, 'agenda/editar_contacto.html', {'form': form, 'contacto': contacto})

def eliminar_contacto(request, contacto_id):
    contacto = Contacto.objects.get(id=contacto_id)
    if request.method == 'POST':
        contacto.delete()
        return redirect('lista_contactos')
    return render(request, 'agenda/eliminar_contacto.html', {'contacto': contacto})

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lista_contactos')
    return render(request, 'agenda/iniciar_sesion.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('iniciar_sesion')