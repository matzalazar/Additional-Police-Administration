"""administracion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from users import views as user_views
from mensajes import views as mensajes_views
from cores import views as cores_views
from polads import views as polads_views

urlpatterns = [
    # HOME
    path('admin/', admin.site.urls),
    path('', views.home, name='home-page'),
    path('dudas/', views.dudas, name='dudas'),
    path('contacto/', views.contacto, name='contacto'),

    # USUARIOS
    path('sendjson/', user_views.send_json, name='send_json'),
    path('register/', user_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),

    # PASSWORDS
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name="password_reset"),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name="password_reset_confirm"),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name="password_reset_complete"),

    path('profile/', user_views.profile, name="profile"),
    path('profile-update/', user_views.profile_update, name="profile-update"),

    # MENSAJES
    path('mis-mensajes/', mensajes_views.mis_mensajes, name="mis-mensajes"),
    path('nuevo-mensaje/', mensajes_views.nuevo_mensaje, name="nuevo-mensaje"),
    path('ver-mensaje/<int:mensaje>/', mensajes_views.mensaje_completo, name="mensaje-completo"),

    # CORES
    path('agregar-cores/', cores_views.agregar_cores, name="agregar-cores"),
    path('ver-cores/', cores_views.ver_cores, name="ver-cores"),
    path('cupo-cores/', cores_views.cupo_cores, name="cupo-cores"),
    path('deletecores/<int:field>/', cores_views.deletecores, name="delete-cores"),
    path('rendir-cores/', cores_views.rendir_cores, name="rendir-cores"),

    # POLADS
    path('nuevo-adicional/', polads_views.nuevo_adicional, name="nuevo-adicional"),
    path('mis-adicionales/', polads_views.mis_adicionales, name="mis-adicionales"),
    path('agregar-turnos/<str:pk>', polads_views.agregar_turnos, name="agregar-turnos"),
    path('deleteturno/<int:field>/', polads_views.deleteturno, name="delete-turno"),
    path('rendir-adicional/<str:pk>', polads_views.rendir_adicional, name="rendir-adicional"),
    path('exportar/<str:pk>', polads_views.exportar, name="exportar"),
    path('calendario/<str:pk>/<int:year>/<int:month>/', polads_views.calendar, name="calendario"),

    path('descargar/<str:pk>', polads_views.descargar, name="descargar"),
]
