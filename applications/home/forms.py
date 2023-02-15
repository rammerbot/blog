from django import forms

from .models import Suscribers

class SuscribersForm(forms.ModelForm):
    class Meta:
        model = Suscribers
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Ingresa tu Correo...',
                }
            ),
        }