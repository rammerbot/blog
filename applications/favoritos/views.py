from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from django.views.generic import ListView, View, DeleteView
from .models import Favorites
from .models import Entry


class UserPageViews(LoginRequiredMixin, ListView):
    template_name = 'favoritos/favoritos.html'
    context_object_name = 'entradas_user'
    login_url = reverse_lazy('user_app:login')
    
    def get_queryset(self):
       
        return Favorites.objects.entradas_user(self.request.user.id)


class FavoritesView(LoginRequiredMixin,View):
    login_url =reverse_lazy('user_app:login')
    def post(self, request, *args, **kwargs):
    
        usuario =self.request.user    
        entrada = Entry.objects.get(id=self.kwargs['pk'])
        validar = Favorites.objects.validar_favorito(usuario, self.kwargs['pk'])
        """validacion del registro"""
        
        if not validar:
            Favorites.objects.create(
                user=usuario,
                entry=entrada,
            )
            return HttpResponseRedirect(reverse('favorites_app:favorites'))
        else:
            messages.error(request, 'El articulo ya se encuentra en favoritos')
            return HttpResponseRedirect(reverse('favorites_app:favorites'))  
            
    


class FavoritosDelete(DeleteView):
    model = Favorites
    success_url = reverse_lazy('favorites_app:favorites')