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

    """devuelve una lista de entradas completas y por categoria"""
    def buscar_entradas(self, kword, categorias):
        if len(categorias)>0:
            return self.filter(category__short_name=categorias, title__icontains=kword, public=True).order_by('-create_at')
        else:
            return self.filter(title__icontains=kword, public=True).order_by('-create_at')

class CategoriaManager(models.Manager):
    
    """entrada para obtener categorias"""
    def obtener_categorias(self):
        return self.all()