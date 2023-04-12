from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from core.models import Mueble

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    last_name=forms.CharField(label="Apellido")
    first_name=forms.CharField(label="Nombre")
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','last_name','first_name']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    # Obligatorios
    username=forms.CharField(max_length=20, label='Usuario')
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']

class FormNuevoMueble(forms.ModelForm):
    class Meta:
        model=Mueble
        fields=['nombre','modelo','descripcion','precio','imagen','oferta']
        
    def __init__(self, *args, feedback=None, **kwargs):
        super().__init__(*args, **kwargs)

        if feedback is not None:
            for key, value in feedback.items():
                self.initial[key] = value

