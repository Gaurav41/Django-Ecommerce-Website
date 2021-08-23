from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,User_messages
from math import ceil
from .forms import ContactForm
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
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():  
            try:  
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                message = form.cleaned_data['message']
                user = User_messages(name=name,email=email,message=message)
                user.save()
                return HttpResponse(name +" "+email +" "+message)  
            except:  
                return HttpResponse("Error")
        else:
            return HttpResponse("Enter valid fields")
    else:  
        form = ContactForm()
        params = {'form':form }
        return render(request,"shop/contact.html",params)

def tracker(request):
    return HttpResponse("tracker")

def search(request):
    return HttpResponse("Search")

def productview(request,id):
    product = Product.objects.filter(id=id).first()

    return render(request,'shop/productview.html',{'product':product})

def checkout(request):
    return HttpResponse("Checkout")





