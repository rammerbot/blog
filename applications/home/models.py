from django.db import models
from model_utils.models import TimeStampedModel

# THIRD_APPS 

# Create your models here.

#ventana principal
class Home(models.Model):
    
    title = models.CharField('Titulo', max_length=20)
    description =  models.TextField('Descripcion')
    about_title =  models.CharField('Titutlo nosotros', max_length=50)
    about_text = models.TextField()
    email_contact = models.EmailField('Correo de contacto', blank=True, null=True)
    phone = models.CharField('Telefono de contacto', max_length=20)
    create_at = models.DateTimeField('Fecha de Creacion', auto_now_add=True)
    update_at = models.DateTimeField('Fecha de Actualizacion', auto_now=True)

    class Meta:
        verbose_name = 'Pagina principal'
        verbose_name_plural = 'Paginas principales'

    def __str__(self):
        return self.title

# modelo para suscriptores
class Suscribers(models.Model):

    email = models.EmailField('Correo')
    create_at = models.DateTimeField('Fecha de Creacion', auto_now_add=True)
    update_at = models.DateTimeField('Fecha de Actualizacion', auto_now=True)

    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'

    def __str__(self):
        return self.email

"""formulario contacto"""
class Contact(TimeStampedModel):
    full_name = models.CharField('Nombre', max_length=60)
    email = models.EmailField('Correo')
    message = models.TextField('Mensaje')

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural =  'Contactos'

    def __str__(self):
        return self.full_name
