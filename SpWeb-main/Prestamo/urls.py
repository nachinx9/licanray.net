from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from Prestamo import views

urlpatterns = [
    path('', views.index),
    path('inicio', views.index),
    path('comprar', views.comprar),
    path('login', views.login),
    path('recuperar', views.recuperar),
    path('registro', views.registro),
]

urlpatterns += staticfiles_urlpatterns()