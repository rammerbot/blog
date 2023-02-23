from datetime import datetime, timedelta
from django.template.defaultfilters import slugify
from django.conf import settings
from django.urls import reverse, reverse_lazy
from django.db import models
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

from .managers import ServicioManager
# Create your models here.


class Category(TimeStampedModel):

    category = models.CharField('Categoria', max_length=60)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.category

class Servicio(TimeStampedModel):
    service = models.CharField('Servicio', max_length=60)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    resume = models.TextField('Resumen', max_length=200)
    description = RichTextUploadingField('Descripcion')
    slug = models.SlugField(editable=False, max_length=300)
    image_1 = models.ImageField('Imagen',null=True, upload_to='servicios')
    image_2 = models.ImageField('Imagen',blank=True, null=True, upload_to='servicios')
    image_3 = models.ImageField('Imagen',blank=True, null=True, upload_to='servicios')
    image_4 = models.ImageField('Imagen',blank=True, null=True, upload_to='servicios')
    image_5 = models.ImageField('Imagen',blank=True, null=True, upload_to='servicios')
    objects = ServicioManager()


    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

        """Generar slug unico"""
    def save(self, *args, **kwargs):
        now =  datetime.now()
        totaltime = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconds = int(totaltime.total_seconds())
        slug_unique = f'{self.service}{str(seconds)}'
        self.slug = slugify(slug_unique)
        super(Servicio, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('servicios_app:detail', kwargs = {
            'slug':self.slug
            })

    def __str__(self):
        return self.service