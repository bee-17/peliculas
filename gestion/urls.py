from django.urls import path
from . import views

urlpatterns = [
    # Películas
    path('peliculas/', views.pelicula_list, name='pelicula_list'),
    path('peliculas/nueva/', views.pelicula_create, name='pelicula_create'),
    path('peliculas/editar/<int:pk>/', views.pelicula_edit, name='pelicula_edit'),
    path('peliculas/eliminar/<int:pk>/', views.pelicula_delete, name='pelicula_delete'),
    # Directores
    path('directores/', views.director_list, name='director_list'),
    path('directores/nuevo/', views.director_create, name='director_create'),
    path('directores/editar/<int:pk>/', views.director_edit, name='director_edit'),
    path('directores/eliminar/<int:pk>/', views.director_delete, name='director_delete'),
]