from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView, LogoutView

from Inventario import views

urlpatterns = [
    path('', views.dashboard),
    path('dashboard', views.dashboard),
    path('login/', LoginView.as_view(template_name='Inventario/login.html'), name = 'login'),
    path('recuperar', views.recuperar),
]

urlpatterns += staticfiles_urlpatterns()