from django.shortcuts import render
from .models import Libro

# Create your views here.

def index(request):
    libros = Libro.objects.all()
    return render(request, 'GestionLibros/index.html', {'libros':libros})

def contacto(request):
    return render(request, 'GestionLibros/contacto.html',{})

def nosotros(request):
    return render(request, 'GestionLibros/nosotros.html',{})