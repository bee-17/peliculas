from django.shortcuts import render, get_object_or_404, redirect
from .models import Pelicula, Director
from .forms import PeliculaForm, DirectorForm

# ──────────── PELÍCULAS ────────────

def pelicula_list(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'gestion/pelicula_list.html', {'peliculas': peliculas})

def pelicula_create(request):
    form = PeliculaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('pelicula_list')
    return render(request, 'gestion/form.html', {'form': form, 'titulo': 'Nueva Película'})

def pelicula_edit(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    form = PeliculaForm(request.POST or None, instance=pelicula)
    if form.is_valid():
        form.save()
        return redirect('pelicula_list')
    return render(request, 'gestion/form.html', {'form': form, 'titulo': 'Editar Película'})

def pelicula_delete(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.method == 'POST':
        pelicula.delete()
        return redirect('pelicula_list')
    return render(request, 'gestion/confirm_delete.html', {'objeto': pelicula, 'tipo': 'película'})

# ──────────── DIRECTORES ────────────

def director_list(request):
    directores = Director.objects.all()
    return render(request, 'gestion/director_list.html', {'directores': directores})

def director_create(request):
    form = DirectorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('director_list')
    return render(request, 'gestion/form.html', {'form': form, 'titulo': 'Nuevo Director'})

def director_edit(request, pk):
    director = get_object_or_404(Director, pk=pk)
    form = DirectorForm(request.POST or None, instance=director)
    if form.is_valid():
        form.save()
        return redirect('director_list')
    return render(request, 'gestion/form.html', {'form': form, 'titulo': 'Editar Director'})

def director_delete(request, pk):
    director = get_object_or_404(Director, pk=pk)
    if request.method == 'POST':
        director.delete()
        return redirect('director_list')
    return render(request, 'gestion/confirm_delete.html', {'objeto': director, 'tipo': 'director'})