from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Mensaje
from .forms import NuevoMensaje

# Create your views here.

@login_required
def mis_mensajes(request):
    mensajes = Mensaje.objects.filter(destinatario=request.user).order_by('-pk')
    context = {'mensajes': mensajes}
    return render(request, 'mensajes/mis_mensajes.html', context)

@login_required
def mensaje_completo(request, mensaje):
    mensaje_completo = Mensaje.objects.get(id=mensaje)
    context = {'mensaje_completo': mensaje_completo}
    return render(request, 'mensajes/ver_mensaje.html', context)

@login_required
def nuevo_mensaje(request):
    form = NuevoMensaje()
    if request.method == 'POST':
        form = NuevoMensaje(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.remitente = request.user
            instance.save()
            messages.success(request, f'{request.user} tu mensaje para {instance.destinatario} ha sido enviado.')
            return redirect('mis-mensajes')
        else:
            print(form.errors.items())
    context = {'form': form}
    return render(request, 'mensajes/nuevo_mensaje.html', context)
