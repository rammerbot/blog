from applications.home.models import Home
from applications.ventas.models import Carrito


# Proceso para recuperar datos de contactos de la empresa

def home_contact(request):
    home = Home.objects.latest('create_at')

    return {
        'phone_contact': home.phone,
        'email_contact': home.email_contact,
    }

def carrito(request):
    user_id = request.user.id
    
    carrito = Carrito.objects.filter(user_id=user_id, product__public=True)
    count =0
    for c in carrito:
        count +=1

    return {
        'carrito_content':carrito,
        'count': count
    }


