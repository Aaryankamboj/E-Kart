from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.

def home(request):
    params={
        'product':Product.objects.all()
    }
    return render(request, 'shop/home.html', params)

def index(request):
    return render(request, 'shop/index.html')


def basic(request):
    return render(request, 'shop/basic.html')

def about(request):
    return HttpResponse("about page")

def contact(request):
    return HttpResponse("Contact Page")

def tracker(request):
    return HttpResponse("tracker page")
    
def search(request):
    return HttpResponse("search page")

def productview(request):
    return HttpResponse("productview page")

def checkout(request):
    return HttpResponse("checkout page")