from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.



# vista para el index

class IndexView(LoginRequiredMixin,TemplateView):
    template_name = 'layout.html'
    login_url = reverse_lazy('user_app:login')
    
