from django.db import models


class EntryManager(models.Manager):
    """procedimiento para entrada"""

    def entrada_portada(self):
        return self.filter(public=True,portada=True).order_by('-create_at').first()

    """devuelve las ultimas 4 entradas en el home"""

    def entradas_home(self):
        return self.filter(public=True, in_home=True).order_by('-create_at')[:4]

    """devuelve las ultimas 6 entradas recientes"""
    def entradas_recientes(self):
        return self.filter(public=True,in_home=True).order_by('-create_at')[:6]
    
