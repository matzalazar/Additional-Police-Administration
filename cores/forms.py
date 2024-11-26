from django import forms
from django.contrib.auth.models import User
from .models import Cores
from administracion.models import Efectivo
from datetime import datetime

# form for add new cores

class AgregarCores(forms.ModelForm):

    ingreso = forms.DateTimeField()
    egreso = forms.DateTimeField()
    efectivo = forms.CharField()

    class Meta:
        model = Cores
        fields = '__all__'
        exclude = ['dependencia']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        e_id = self.initial.get('efectivo', None)
        if e_id:
            self.initial['efectivo'] = Efectivo.objects.get(id=_id).efectivo_nombre

        self.fields['ingreso'].widget.attrs['type'] = 'datetime'
        self.fields['egreso'].widget.attrs['type'] = 'datetime'

    def clean(self):
        try:
            e = Efectivo.objects.get(efectivo_nombre=self.cleaned_data['efectivo'])
        except Efectivo.DoesNotExist:
            pass
        self.cleaned_data['efectivo'] = e

        return self.cleaned_data  # Return self.cleaned_data at the end of clean()
