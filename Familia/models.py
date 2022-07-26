from unicodedata import name
from django.db import models
from datetime import datetime

class Familia(models.Model):
    name= models.CharField(max_length=40)#Nombre
    last_name= models.CharField(max_length=40)#Apellido
    age=models.IntegerField()#Edad
    dni=models.IntegerField(unique=True,null=True, blank=True)#dni, pongo unique para que no pueda ingresarme dos personas con el mismo dni     
    birthday_date=models.DateField(auto_now_add=False, null=True, blank=True)#Fecha de nacimientos
    