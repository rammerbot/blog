from applications.home.models import Home


# Proceso para recuperar datos de contactos de la empresa

def home_contact(request):
    home = Home.objects.latest('create_at')

    return {
        'phone_contact': home.phone,
        'email_contact': home.email_contact,
    }