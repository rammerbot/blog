from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'favorites_app'
urlpatterns = [
    path('favorites/', views.UserPageViews.as_view(), name='favorites'),
    path('favorites_add/<pk>/', views.FavoritesView.as_view(), name='favorites_add'),
    path('delete_entry/<pk>/', views.FavoritosDelete.as_view(), name='delete_entry'),
]