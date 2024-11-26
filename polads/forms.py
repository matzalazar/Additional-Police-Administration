from django import forms
from django.contrib.auth.models import User
from administracion.models import Comisaria, Efectivo
from .models import Adicional, Turno

# form to add new polad

class AddAdicional(forms.ModelForm):

    numero = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-polad'}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-polad'}))
    domicilio = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-polad'}))
    entidad_contratante = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-polad'}))
    cuenta_corriente = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-polad'}))
    comisaria = forms.ModelChoiceField(queryset=Comisaria.objects.filter(es_cabecera=True))

    class Meta:
        model = Adicional
        fields = '__all__'
        exclude = ['encargado', 'puede_rendir']

class AddTurno(forms.ModelForm):

    ingreso = forms.DateTimeField()
    egreso = forms.DateTimeField()
    efectivo = forms.CharField()

    class Meta:
        model = Turno
        fields= '__all__'
        exclude = ['polad']

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
