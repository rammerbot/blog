from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'user_app'
urlpatterns = [
    path('create_user/',views.CreateUserView.as_view(), name='create_user'),
    path('login/',views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('user_update/<username>/',views.UserUpdateView.as_view(), name='user_update'),
    path('activate/<pk>/', views.ConfirmacionView.as_view(), name='activate'),
]