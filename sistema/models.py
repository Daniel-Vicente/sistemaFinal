from django.db import models

class Cine(models.Model):
    nombreCine = models.CharField(max_length=200)
    direccionCine = models.CharField(max_length=200)
    telefonoCine = models.CharField(max_length=50)
    emailCine = models.CharField(max_length=200)
    

class TipoSala(models.Model):
    nombreTipoSala = models.CharField(max_length=200)

class Sala(models.Model):
    nombre_sala = models.CharField(max_length=200)
    id_tipoSala = models.ForeignKey(TipoSala, on_delete=models.CASCADE)
    id_cine = models.ForeignKey(Cine, on_delete=models.CASCADE)


class Fila(models.Model):
    nombre = models.CharField(max_length=200)
    id_sala = models.ForeignKey(Sala, on_delete=models.CASCADE)


class Pelicula(models.Model):
    nombrePelicula = models.CharField(max_length=200)
    Descripcion = models.CharField(max_length=200)
    id_sala = models.ForeignKey(Sala, on_delete=models.CASCADE)