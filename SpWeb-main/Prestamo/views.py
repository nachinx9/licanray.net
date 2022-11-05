from django.shortcuts import render

def index(request):
    return render(request, "Prestamo/index.html")

def comprar(request):
    return render(request, "Prestamo/comprar.html")

def login(request):
    return render(request, "Prestamo/login.html")

def recuperar(request):
    return render(request, "Prestamo/recuperar.html")
    
def registro(request):
    return render(request, "Prestamo/registro.html")