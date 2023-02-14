# propias del sistema
from django.shortcuts import render
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
# locales
from .models import User

class CreateUserForm(forms.ModelForm): 
    # creacionde campos para ingresar contraseñas y la verificacion 
    password1 = forms.CharField(
        label="Ingrese contraseña: ",
        required=True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña...'
            }
        )
    )

    password2 = forms.CharField(
        label="Confirmar contraseña: ",
        required=True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'Confirme su Contraseña...'
            }
        )
    )

    def clean_password2(self):

        if len(self.cleaned_data['password1'])< 8:
            self.add_error('password1', 'La contraseña debe tener de almenos 8 caracteres')
        elif self.cleaned_data['password2'] != self.cleaned_data['password1']:
            self.add_error('password2', 'La contraseña no coincide' )
        

    # Seleccionar campos a mostrar
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'nombre',
            'apellido',
            'ocupacion',
            'date_brth',
            'gender',
        )

# Formulario para Login

class LoginForm(forms.Form):

    email = forms.CharField(
        label="Correo: ",
        required=True,
        widget= forms.TextInput(
            attrs={
                'placeholder': 'Usuario...'
            }
        )
    )

    password = forms.CharField(
        label="contraseña: ",
        required=True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña...'
            }
        )
    )
    
    # mensaje de error al introducir un valor errado

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('El correo y/o la contraseña son incorrectos')

        return cleaned_data

# formulario para el cambio de datos

class UserUdateForm(forms.Form):

    old_password = forms.CharField(
        label="Contraseña actual: ",
        required=True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'ingrese contraseña...'
            }
        )
    )

    new_password = forms.CharField(
        label="Contraseña nueva: ",
        required=True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña...'
            }
        )
    )
    new_password2 = forms.CharField(
        label="Confirme contraseña: ",
        required=True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña...'
            }
        )
    )


    def __init__(self, username, *args, **kwargs):
        self.username = username
        super(UserUdateForm, self).__init__(*args, **kwargs)

    def clean_new_password2(self):
        # verificacion de contaseña actual
        password = User.objects.password_validator(self.username)

        if not check_password(self.cleaned_data['old_password'], password):
            self.add_error('old_password', 'La contraseña es incorrecta' )
        # verificacion de contaseña nueva
        elif len(self.cleaned_data['new_password'])< 8:
            self.add_error('new_password', 'La contraseña debe tener de al menos 8 caracteres')
        elif self.cleaned_data['new_password2'] != self.cleaned_data['new_password']:
            self.add_error('new_password2', 'La contraseña no coincide' )

# Formulario para la activacion

class ActivateForm(forms.Form):

    code_register = forms.CharField(required=True)

    def __init__(self, pk, *args, **kwargs):
        self.id_user = pk
        super(ActivateForm, self).__init__(*args, **kwargs)

    def clean_code_register(self):
        codigo = self.cleaned_data['code_register']
        
        if len(codigo) == 6:
            activo = User.objects.code_validation(self.id_user, codigo)
            if not activo:
                raise forms.ValidationError('El codigo es incorrecto')
        else:
            raise forms.ValidationError('El codigo es incorrecto')
        
   