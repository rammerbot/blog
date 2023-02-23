from django.db import models
from django.conf import settings

from applications.entrada.models import Entry
from .managers import FavoritesManager

# Create your models here.


class Favorites(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_favorites", on_delete=models.CASCADE)
    entry = models.ForeignKey(Entry, related_name='entry_favorites', on_delete=models.CASCADE)
    create_at = models.DateTimeField('Fecha de Creacion', auto_now_add=True)
    update_at = models.DateTimeField('Fecha de Actualizacion', auto_now=True)
    objects = FavoritesManager()

    class Meta:
        verbose_name = "Favorito"
        verbose_name_plural = "Favoritos"
        unique_together = ('user', 'entry')
        
    def __str__(self):
        return f"{self.user.username}  -  {self.entry}"
