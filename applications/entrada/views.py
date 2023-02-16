from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Entry, Category
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class EntryListView(ListView):
    template_name = "entrada/lista.html"
    context_object_name = 'entradas'
    paginate_by = 10

    """obtener contexto desde cualquier modulo"""
    def get_context_data(self, **kwargs):

        context = super(EntryListView, self).get_context_data(**kwargs)
        context['categorias']= Category.objects.obtener_categorias()
        return context

    """obtener datos a traves de un buscador en el template"""
    def get_queryset(self):
        kword = self.request.GET.get('kword','')
        categoria = self.request.GET.get('categorias','')
        # consulta de busqueda
        resultado = Entry.objects.buscar_entradas(kword, categoria)
        return resultado

class EntryDetail(DetailView):
    template_name = 'entrada/detail.html'
    model = Entry
    context_object_name = 'entrada'
    
