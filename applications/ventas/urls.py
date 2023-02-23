from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'ventas_app'
urlpatterns = [
   path('products/', views.ProductList.as_view(), name='products'),
   path('product/<slug>', views.ProductDetail.as_view(), name='product'),
   path('carrito/', views.CarritoView.as_view(), name='carrito'),
   path('carrito_add/<pk>', views.CarritoAdd.as_view(), name='carrito_add'),
   path('product_delete/<pk>', views.DeleteProduct.as_view(), name='product_delete'),
]