from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Category, Servicio
# Create your views here.


class ServiciosView(ListView):
    template_name = 'servicios/servicio_list.html'
    model = Servicio
    context_object_name = 'servicio'

    def get_context_data(self, **kwargs):
        context =  super(ServiciosView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
           
        return context
    
class ServicioDetail(DetailView):
    template_name = 'servicios/servicio_detail.html'
    model = Servicio

    def get_context_data(self, *args, **kwargs):
        context =  super(ServicioDetail, self).get_context_data(*args, **kwargs)
        slug = self.kwargs['slug']
        servicio = Servicio.objects.filter(slug=slug)
        print('****************************************************************')
        for i in servicio:
            try:
                context['image1'] = i.image_1.url
            except:
                break  
            try:
                context['image2'] = i.image_2.url
            except:
                break
            try:
                context['image3'] = i.image_3.url
            except:
                break
            try:
                context['image4'] = i.image_4.url
            except:
                break
            try:
                context['image5'] = i.image_5.url
            except:
                break
         
        return context
