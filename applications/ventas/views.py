from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView,DeleteView, DetailView, View
from .models import Product, Category, Carrito

# Create your views here.


class ProductList(ListView):

    template_name = 'ventas/products_list.html'
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['categorys']= Category.objects.get_category_product()
        return context

    def get_queryset(self):
        
        kword = self.request.GET.get('kword','')
        # valor obtenido a traves de la etiqueta link en las categorias del html
        categorias = self.request.GET.get('categorias','')
        resultado = Product.objects.get_products(kword, categorias)
    
        return resultado

        
class ProductDetail(DetailView):
    template_name = 'ventas/product_detail.html'
    context_object_name = "product"
    model = Product


class CarritoView(ListView):

    template_name = 'ventas/carrito.html'
    context_object_name ='products'

    model = Carrito

class CarritoAdd(View):
    
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('user_app:login')
        else:
            user = self.request.user
            product = Product.objects.get(id=self.kwargs['pk'])
            Carrito.objects.create(
                user=user,
                product=product
            )
            return HttpResponseRedirect(reverse('ventas_app:carrito'))

class DeleteProduct(DeleteView):
    model=Carrito
    success_url=reverse_lazy('ventas_app:carrito')



