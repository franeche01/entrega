
from django.urls import path
from . import views

urlpatterns = [
    path('insertar/autor/', views.insertar_autor, name='insertar_autor'),
    path('insertar/categoria/', views.insertar_categoria, name='insertar_categoria'),
    path('insertar/libro/', views.insertar_libro, name='insertar_libro'),
    path('buscar/', views.buscar_libro, name='buscar_libro'),
]
