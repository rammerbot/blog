from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'home_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('suscripcion', views.SuscribersView.as_view(), name='suscripcion'),
    path('error', views.ContactView.as_view(), name='error'),
    path('contact/', views.ContactView.as_view(), name='contact')
]