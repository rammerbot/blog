from django.db import models
from datetime import datetime, timedelta
from django.template.defaultfilters import slugify
from django.conf import settings
from django.urls import reverse, reverse_lazy
from ckeditor_uploader.fields import RichTextUploadingField
from model_utils.models import TimeStampedModel

from .managers import ProductManager, CategoryManager

# Create your models here.

class Category(TimeStampedModel):
    category = models.CharField('Categoria',max_length=30)
    objects = CategoryManager()
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.category
        

class Product(TimeStampedModel):
    product = models.CharField('Producto', max_length=60)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField('Precio', max_digits=10, decimal_places=2)
    image = models.ImageField('Imagen', upload_to='productos')
    description = RichTextUploadingField('Descripcion')
    public = models.BooleanField('Disponible', default=False)
    slug = models.SlugField(editable=False, max_length=300)
    active = models.BooleanField('Activo', default=True)
    objects = ProductManager()

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    """Generar slug unico"""
    def save(self, *args, **kwargs):
        now =  datetime.now()
        totaltime = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconds = int(totaltime.total_seconds())
        slug_unique = f'{self.product}{str(seconds)}'
        self.slug = slugify(slug_unique)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('ventas_app:product', kwargs = {
            'slug':self.slug
            })

    def __str__(self):
        return self.product
        

class Carrito(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_product', on_delete=models.CASCADE)
    product =models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Carrito'
        verbose_name_plural = 'Carritos'

    def __str__(self):
        return f"{self.user.username}  -  {self.product}"
