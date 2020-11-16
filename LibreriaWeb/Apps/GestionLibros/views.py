from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from .models import Libro

# Create your views here.

def index(request):
    libros = Libro.objects.all()
    paginator = Paginator(libros,12)
    num_pagina = request.GET.get('page')
    obj_pagina = paginator.get_page(num_pagina)

    return render(request, 'GestionLibros/index.html', {'obj_pagina':obj_pagina})

def contacto(request):
    return render(request, 'GestionLibros/contacto.html',{})

def nosotros(request):
    return render(request, 'GestionLibros/nosotros.html',{})