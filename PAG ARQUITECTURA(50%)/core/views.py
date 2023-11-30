from django.shortcuts import render
from .models import *
from django.contrib.auth.views import logout_then_login
from .forms import *
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.
def registro(request):
    if request.method == "POST":
        form = Registro(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:        
        form = Registro()
    return render(request, 'core/registro.html', {'form':form})

def home(request):
    return render(request, 'core/index.html')

def home2(request):
    return render(request, 'core/home/index.html')
def registroropa(request):
    form = Ropa(request.POST)
    return render(request, 'core/registroropa.html', {'form':form})

def logout(request):
    return logout_then_login(request, login_url="home")
    

def comprar(request):
    carro = request.session.get("carro", [])
    total = 0
    for c in carro:
        total += c[5]
    venta = Estado()
    venta.cliente = request.user
    venta.total = total
    venta.save()
    # Guardamos cada producto en la tabla detalle
    for c in carro:
        producto= Ropa.objects.get(codigo=c[0])
        Historial = Historial()
        Historial.venta = venta
        Historial.Ropa = Ropa.objects.get(codigo=c[0])
        Historial.cantidad = c[2]
        Historial.precio = c[1]
        Historial.total = c[5]
        Historial.save()
        producto.stock=producto.stock - c[2]
        producto.save()
    request.session["carro"] = []
    return redirect(to="carrito")

def historial(request):
    if not request.user.is_authenticated:
        return redirect(to="login")
    compras = Estado.objects.filter(cliente=request.user)
    return render(request, 'core/historial.html', {"compras":compras})
