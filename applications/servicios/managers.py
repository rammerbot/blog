from django.db import models


class ServicioManager(models.Manager):

    def imagenes_servicios(self, slug):
        return self.filter(slug=slug)
