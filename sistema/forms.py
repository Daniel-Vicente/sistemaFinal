from django.db import models
from django.forms import ModelForm
from .models import Cine

#class PeliculaForm(ModelForm):
 #  class Meta:
#      model = Pelicula
#      fields = '__all__'

class CineForm(ModelForm):
   class Meta:
      model = Cine
      fields = '__all__'