from django import forms
from django.contrib.auth.models import User
from .models import Mensaje

class NuevoMensaje(forms.ModelForm):

    mensaje = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-polad'}))

    class Meta:
        model = Mensaje
        fields = '__all__'
        exclude = ['remitente', 'creado']
