from django.shortcuts import render
from . import models

def home_page(request):
    return render(request,'index.html')

def view_provider_page(request):
    queryset = models.Proveedor.objects.all()
    return render(request,'provider.html',{'provider':queryset})

def home_page_admin(request):
    return render(request,'home_admin.html')