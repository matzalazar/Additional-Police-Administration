from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'administracion/home.html')

def dudas(request):
    return render(request, 'administracion/dudas.html')

def contacto(request):
    return render(request, 'administracion/contacto.html')
