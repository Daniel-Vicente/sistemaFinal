from django.shortcuts import render, redirect, get_list_or_404

import cinemapplication
from .models import  Cine, Pelicula, Sala
from .forms import  CineForm

""" def listaPeliculas(request):
   peliculas = Pelicula.objects.all()
   salas = Sala.objects.all();

   context = {
      'peliculas': peliculas,
      'salas': salas,
      'form': PeliculaForm()
   }
   
   return render(request, 'polls/pelicula.html',context) """


""" def crearPelicula(request):
   form = PeliculaForm(request.POST)  

   if form.is_valid():  
      try:  
         form.save() 
         return redirect('list_Peliculas')
      except:  
         pass  

   return redirect('list_Peliculas') """


""" def actualizarPelicula(request, id):  
   pelicula = Pelicula.objects.get(id=id)

   print(pelicula)

   form = PeliculaForm(initial={
      'nombre': pelicula.nombrePelicula, 
      'Descripcion': pelicula.Descripcion, 
      'id_sala': pelicula.id_sala}
   )

   if form.is_valid():  
      try:  
         form.save() 
         return redirect('/list_Peliculas')  
      except Exception as e: 
         pass    
   return render(request,'pelicula.html',{'form':form})   """


""" def eliminarPelicula(request, pelicula_id):
   pelicula = Pelicula.objects.get(pk=pelicula_id)
   pelicula.delete()

   return redirect('list_Peliculas') """
   


   


def listaCine(request):
   cines = Cine.objects.all();
   #salas = Sala.objects.all();

   context = {
      'cines': cines,
      'form': CineForm()
   }
   
   return render(request, 'polls/cine.html',context)


def crearCine(request):
   form = CineForm(request.POST)  

   if form.is_valid():  
      try:  
         form.save() 
         return redirect('listCines')
      except:  
         pass  

   return redirect('listCines')


def actualizarCine(request, id):  
   cine = Cine.objects.get(id=id)

   print(cine)

   form = CineForm(initial={
      'nombre': cine.nombreCine, 
      'Direccion': cine.direccionCine, 
      'Telefono': cine.telefonoCine,
      'Email': cine.emailCine}
   )

   if form.is_valid():  
      try:  
         form.save() 
         return redirect('/listCines')  
      except Exception as e: 
         pass
   return render(request,'cine.html',{'form':form})  


def eliminarCine(request, cine_id):
   cine = Cine.objects.get(pk=cine_id)
   cine.delete()

   return redirect('listCines')
   

   