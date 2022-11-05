from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Inventario.models import User

# Create your views here.

'''def login(request):
    return render(request, "Inventario/login.html")'''

def recuperar(request):
    return render(request, "Inventario/recuperar.html")

@login_required(login_url="login")
def dashboard(request):
    return render(request, "Inventario/dashboard.html")

