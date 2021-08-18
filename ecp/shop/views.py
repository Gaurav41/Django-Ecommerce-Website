from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.

def index(request):
    # products = Product.objects.all()
    # n = len(products)
    # slides = n//4 + ceil((n/4)-(n//4))
    # # params = {'no_of_slides':slides,'range','product':products}
    # all_prods = [[products,range(1,slides),slides],
    #              [products,range(1,slides),slides]]

    all_prods = []
    catprods= Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        slides = n//4 + ceil((n/4)-(n//4))
        all_prods.append([prod,range(1,slides),slides])


    params = {"all_prods":all_prods}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("Contact us")

def tracker(request):
    return HttpResponse("tracker")

def search(request):
    return HttpResponse("Search")

def productview(request):
    return HttpResponse("Productview ")

def checkout(request):
    return HttpResponse("Checkout")





