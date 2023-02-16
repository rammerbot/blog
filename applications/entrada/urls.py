from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'entrada_app'
urlpatterns = [
   path('entradas/', views.EntryListView.as_view(), name='entradas'),
   path('detail/<slug>/', views.EntryDetail.as_view(), name='detail'),
]