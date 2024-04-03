from django.shortcuts import redirect, render
from django.http import HttpResponse
from .. import models
import json

def cashier_page(request):
    if request.session.get('cajero'):
        cashier = models.Cajero.objects.get(idCajero = request.session.get('id'))
        return render(request,'cashier/home_cash.html', {'data': cashier, 'color': 'danger'})
    else: 
        return redirect('/singout/')
    
def inventory_page(request):
    if request.session.get('cajero'):
        cashier = models.Cajero.objects.get(idCajero = request.session.get('id'))
        products = models.Producto.objects.all()
        return render(request,'cashier/inventario.html', {'data': cashier, 'color': 'danger', 'products' : products})
    else: 
        return redirect('/singout/')
    
def getProductByID(request):
    if request.session.get('cajero'):
        print("si")
    else: 
        return redirect('/singout/')
    