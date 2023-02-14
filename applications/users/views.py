from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic import FormView, TemplateView, View
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .forms import CreateUserForm, LoginForm, UserUdateForm, ActivateForm

from .models import User
from .funtions import code_generator
# Create your views here.

# vista para la creacion de usuarios con Formview

class CreateUserView(FormView):
    template_name = 'user/create_user.html'
    form_class = CreateUserForm
    success_url = '#'

    def form_valid(self, form):

        #generar codigo
        codigo = code_generator()

        usuario = User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombre = form.cleaned_data['nombre'],
            apellido = form.cleaned_data['apellido'],
            ocupacion = form.cleaned_data['ocupacion'],
            date_brth = form.cleaned_data['date_brth'],
            code_register = codigo,
            gender = form.cleaned_data['gender']
        )
        # enviar codigo por email
        asunto = 'Confirmacion de Email'
        mensaje = f'El codigo de verificaciones es: {codigo}'
        remitente = 'apuestaselviejo@gmail.com'
        send_mail(asunto, mensaje, remitente,[form.cleaned_data['email'],])
        return HttpResponseRedirect(reverse('user_app:activate', kwargs={'pk':usuario.id}))

       

# vista del login

class LoginView(FormView):
    template_name = 'user/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:index')

    def form_valid(self, form):
        
        user =  authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginView, self).form_valid(form)

# vista del logout

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)

        return HttpResponseRedirect(
            reverse('user_app:login')
        )

# vista de actualizacion de datos

class UserUpdateView(FormView):
    template_name = 'user/user_update.html'
    form_class = UserUdateForm
    success_url = reverse_lazy('user_app:login')

    def get_form_kwargs(self):
    
        kwargs = super(UserUpdateView, self).get_form_kwargs()
        kwargs.update({'username': self.kwargs['username']})
        return kwargs
    
    def form_valid(self, form):
        usuario = self.request.user
        user =  authenticate(
            email=usuario.email,
            password=form.cleaned_data['old_password']        
        )

        if user:
            new_password = form.cleaned_data['new_password']
            usuario.set_password(new_password)
            usuario.save()
            logout(self.request)
            
        return super(UserUpdateView, self).form_valid(form)

# Activacion de cuenta mediante codigo

class ConfirmacionView(FormView):
    template_name = 'user/activate.html'
    form_class = ActivateForm
    success_url = reverse_lazy('user_app:login')

    def get_form_kwargs(self):
        kwargs = super(ConfirmacionView, self).get_form_kwargs()
        kwargs.update({'pk':self.kwargs['pk']})
        return kwargs
        
    def form_valid(self, form):

        User.objects.filter(id=self.kwargs['pk']).update(is_active=True)
       
        return super(ConfirmacionView, self).form_valid(form)