from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from applications.entrada.models import Entry
from .models import Home
from .forms import SuscribersForm, ContactForm
# Create your views here.



# vista para el index

"""class IndexView(LoginRequiredMixin,TemplateView):
    template_name = 'layout.html'
    login_url = reverse_lazy('user_app:login')"""

class IndexView(TemplateView):
    """vista de pagina de inicio"""

    template_name = 'home/index.html'

    # obtener contexo de la base de datos

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        #texto de portada
        context['home'] = Home.objects.latest('-create_at')
        context["portada"]= Entry.objects.entrada_portada()
        context['entradas_home']= Entry.objects.entradas_home()
        context['entradas_recientes']=Entry.objects.entradas_recientes()
        context['form'] = SuscribersForm
        return context

class SuscribersView(CreateView):
    form_class = ContactForm
    success_url = '.'
    

class ContactView(CreateView):
    form_class = ContactForm
    success_url = reverse_lazy('home_app:index')
    


    
