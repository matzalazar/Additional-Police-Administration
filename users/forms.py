from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from administracion.models import Efectivo
from datetime import datetime

# form for the new users records

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def __init__(self, *args, **kwargs):

        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):

        user = super(UserRegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

# form for update users profiles

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['phone_number', 'tipo_usuario', 'administrador_de']

    def clean(self):

        cleaned_data = super(ProfileUpdateForm, self).clean()

        tipo_usuario = self.cleaned_data.get('tipo_usuario')
        administrador_de = self.cleaned_data.get('administrador_de')

        if tipo_usuario == 'Administrador' and administrador_de == None:
            raise forms.ValidationError('Indicar Comisaría de la que sos responsable de la Oficina de Adminsitración.')
        elif tipo_usuario == 'Encargado' and administrador_de != None:
            raise forms.ValidationError('No indicar Comisaría. Deben hacerlo sólo aquellos responsables de la Oficina de Administración.')

        return self.cleaned_data
