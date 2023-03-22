from django.shortcuts import redirect, render
from recetas.forms import RecestasForm

from recetas.models import Categoria, Receta

# Create your views here.
def index(request):
    """
    - HOME
    Listo todas las categorias que hay en la tabla recetas_categoria
    """
    categorias = Categoria.objects.all().order_by('-id')

    context = {
        'categorias': categorias
    }
    
    return render(request, 'recetas/index.html', context)


def listado(request, cat_id):
    """
    - LISTADO
    Listo todas las recetas filtradas por la categoria id recibida por parametro (cat_id)
    """
    recetas = Receta.objects.filter(categoria_id=cat_id)

    context = {
        'recetas': recetas
    }
    
    return render(request, 'recetas/listado.html', context)


def create(request):
    """
    - CREATE
    Creo nueva receta a través del formulario forms.py.RecestasForm()
    """
    form = RecestasForm()

    if request.method == 'POST':
        form = RecestasForm(request.POST)
        if form.is_valid():
            instance = form.save()
            
            return redirect('recetas:read', instance.id)

    context = {
        'form': form
    }
    
    return render(request, 'recetas/create.html', context)


def read(request, rec_id):
    """
    - READ
    Muestro los datos que hay en la tabla recetas_receta de una receta 
    según la receta id pasada por parámetro (rec_id)
    """
    receta = Receta.objects.get(id=rec_id)

    context = {
        'receta': receta
    }

    return render(request, 'recetas/read.html', context)


def update(request, rec_id):
    """
    - UPDATE
    Obtengo la receta segun receta id (rec_id).
    Paso la receta al formulario (instance=receta)
    POST: Actualizo los datos en la tabla
    """

    receta = Receta.objects.get(id=rec_id)
     
    form = RecestasForm(instance=receta)

    if request.method == 'POST':
        form = RecestasForm(request.POST, instance=receta)
        if form.is_valid():
            instance = form.save()
            
            return redirect('recetas:read', instance.id)


    context = {
        'form': form
    }

    return render(request,'recetas/update.html', context)


def delete(request, rec_id):
    """
    - DELETE
    Obtengo la receta segun receta id (rec_id).
    Borro la receta de la tabla.
    """

    receta = Receta.objects.get(id=rec_id)

    receta.delete()

    return redirect('recetas:index')
