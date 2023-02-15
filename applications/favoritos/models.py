from django.db import models
from django.conf import settings

from applications.entrada.models import Entry

# Create your models here.


class Favorites(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_favorites", on_delete=models.CASCADE)
    entry = models.ForeignKey(Entry, related_name='entry_favorites', on_delete=models.CASCADE)
    create_at = models.DateTimeField('Fecha de Creacion', auto_now_add=True)
    update_at = models.DateTimeField('Fecha de Actualizacion', auto_now=True)

    class Meta:
        unique_together = ('user', 'entry')
