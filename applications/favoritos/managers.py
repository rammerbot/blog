from django.db import models

class FavoritesManager(models.Manager):


    def entradas_user(self, user):
        """entradas favoritos del usuario"""
        return self.filter(entry__public=True, user=user).order_by('-create_at')

    def validar_favorito(self, user, entry_id):
        """obtener favorito para validacion"""
        return self.filter(user=user, entry__id=entry_id)
