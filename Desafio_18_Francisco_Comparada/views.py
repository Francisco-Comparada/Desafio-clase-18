from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def Inicio (request):
    today= datetime.now().date
    context = {
        'name':' Francisco',
        'last_name':' Comparada',
        'today':today
    }
    return render (request,'template1.html', context=context)
    