from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'servicios_app'
urlpatterns = [
    path('servicios/', views.ServiciosView.as_view(), name='servicios'),
    path('servicio/<slug>', views.ServicioDetail.as_view(), name='servicio'),
]