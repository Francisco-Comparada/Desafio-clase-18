
from django.contrib import admin
from django.urls import path
from Desafio_18_Francisco_Comparada.views import Inicio
from Familia.views import Agregar_familiar, list_family

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/',Inicio,name='Inisscisso'),
    path('agregar_familia/',Agregar_familiar),
    path('lista_familia/',list_family)
]
