from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UseManager 

# Create your models here.


# model para la creacion de usuarios

class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M','Masculino'),
        ('F','Femenino'),
        ('o','Otro')


    )

    username = models.CharField('Nombre de Usuario',max_length=10, unique=True)
    email = models.EmailField('Correo', unique=True)
    nombre = models.CharField('Nombre', max_length=30, blank=True)
    apellido = models.CharField('Apellido', max_length=30,blank=True)
    ocupacion = models.CharField('Ocupacion', max_length=60, blank=True)
    date_brth = models.DateField('Fecha de nacimiento', blank=True, null=True)
    code_register = models.CharField('Codigo de Registro', max_length=6, blank=True)
    gender = models.CharField('Genero', max_length=1, choices=(GENDER_CHOICES), blank=True)
    objects = UseManager()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['username',]


    # obteber valores de los usuarios
    def __str__(self):
        return str(self.id) + ' - ' + self.username + ': ' + self.email

    def get_username(self):
        return self.email
    
    def get_full_name(self):
        return self.nombre + '  ' + self.apellido
    

