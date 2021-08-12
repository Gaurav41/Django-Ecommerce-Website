from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse("about us")

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





