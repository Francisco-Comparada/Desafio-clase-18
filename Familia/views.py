from datetime import datetime
from hmac import new
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from Familia.models import Familia
import datetime

def Agregar_familiar(request):
    #####################################
    #USU PARA CALCULAR EDAD CON LA FECHA DE NACIMIENTO
    birthday= datetime.date(2003,4,4)
    fecha_actual = datetime.date.today()
    age_ = fecha_actual.year - birthday.year
    age_ -= ((fecha_actual.month, fecha_actual.day) < (birthday.month, birthday.day))
    ######################################
   
    new_person = Familia.objects.create(name='Joaquin',last_name='Comparada',dni=44867923,age=age_,birthday_date=birthday)
    context={
        'new_person':new_person
    }
    return render (request,'new_person.html', context=context)


def list_family(request):
    persons = Familia.objects.all()

    context = {
        'persons':persons
    }  
    return render(request, 'family_list.html', context=context)
