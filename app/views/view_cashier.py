from django.shortcuts import redirect, render
from .. import models

def cashier_page(request):
    if request.session.get('cajero'):
        cashier = models.Cajero.objects.get(idCajero = request.session.get('id'))
        return render(request,'cashier/home_cash.html', {'data': cashier, 'color': 'danger'})
    else: 
        return redirect('/singout/')