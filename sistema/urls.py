from django.urls import path

from . import views
import sistema

urlpatterns = [
    #path('peliculas/', views.listaPeliculas, name='list_Peliculas'),
    #path('addPelicula', views.crearPelicula, name='add_Pelicula'),
    #path('<int:pelicula_id>/deletePelicula', views.eliminarPelicula, name='delete_Pelicula'),
    #path('<int:pelicula_id>/updatePelicula', views.actualizarPelicula, name='update_Pelicula'),


    path('', views.listaCine, name='listCines'),
    path('addCine', views.crearCine, name='addCine'),
    path('<int:cine_id>/deleteCine', views.eliminarCine, name='deleteCine'),
    path('<int:cine_id>/updateCine', views.actualizarCine, name='updateCine')
]
