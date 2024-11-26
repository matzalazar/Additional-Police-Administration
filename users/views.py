from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from administracion.models import Efectivo
from django.http import JsonResponse
from django.core import serializers
from datetime import datetime
from .models import Profile
from polads.models import Adicional, Turno
from cores.models import Cores
from mensajes.models import Mensaje

# register form view

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} tu cuenta ha sido creada.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# profile view

@login_required
def profile(request):

    show_turnos = ''
    turnos = ''
    show_cores = ''
    cores = ''
    show_mensajes = ''
    mensajes = ''

    usuario = request.user.profile.tipo_usuario

    # últimos turnos de polad:

    if usuario == 'Encargado':
        turnos = Turno.objects.filter(polad__in=Adicional.objects.filter(encargado=request.user)).order_by('-pk')[:10]
    else:
        turnos = Turno.objects.filter(polad__in=Adicional.objects.filter(comisaria=request.user.profile.administrador_de)).order_by('-pk')[:10]

    # últimas cores y mensajes:

    cores = Cores.objects.filter(dependencia=request.user.profile.administrador_de).order_by('-pk')[:10]
    mensajes = Mensaje.objects.filter(destinatario=request.user).order_by('-pk')[:10]

    # sin registros

    if not turnos:
        show_turnos = "Aún no han sido creados registros."

    if not cores:
        show_cores = "Aún no han sido creados registros."

    if not mensajes:
        show_mensajes = "Aún no recibiste mensajes."

    context = {'turnos': turnos, 'cores': cores, 'mensajes': mensajes, 'show_turnos': show_turnos, 'show_cores': show_cores, 'show_mensajes': show_mensajes}

    return render(request, 'users/profile.html', context)

# update profile view

@login_required
def profile_update(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if u_form.has_changed() or p_form.has_changed():
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f'{request.user} tu perfil ha sido actualizado.')
                return redirect('profile')
        else:
            messages.info(request, f'{request.user} no modificaste información en tu perfil.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile_update.html', context)

# get efectivos list for autocomplete function

def send_json(request):
    e_todos = Efectivo.objects.all()
    json_list = []
    for e in e_todos:
        e_data = {}
        e_data['nombre'] = e.efectivo_nombre
        e_data['jerarquia'] = e.efectivo_jerarquia
        e_data['legajo'] = e.efectivo_legajo
        json_list.append(e_data)
    return JsonResponse(json_list, safe=False)
