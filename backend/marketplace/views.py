from django.shortcuts import render,redirect, HttpResponse
from .models import *
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from .rapyd_apis import make_request

# Create your views here.
def Home(request):
    products_obj = Product.objects.all()
    products = []
    for i in products_obj:
        products.append(model_to_dict(i))

    context = { "items" : products }
    return render(request,'marketplace/productcard.html',context=context)

def ProductsCart(request):
    return render(request,'marketplace/productcard.html')

def ProductsWishlist(request):
    return render(request,'marketplace/productcard.html')

def ProductPage(request,id):
    products_obj = Product.objects.filter(id = id).first()
    product = model_to_dict(products_obj)
    context = product
    print(context)
    return render(request,"marketplace/SingleCard.html",context=context)

@login_required(login_url='Base:Login')
def PaymentDirection(request):
    wallet_body = {
        "amount": 50,
        "currency": "USD",
        "country":"US",
        "complete_payment_url":"Eco_Sotre:Home",
        #Change this github link at the time of production. to the website link
        #Rapyd do not allow urls of local host. Thats why we kept github here
        "complete_checkout_url":"https://www.github.com/anirudh3167",
        "error_payment_url":"store:Failed"
    }
    response = make_request(method='post',path='/v1/checkout',body=wallet_body)
    #print(response)
    hosted_url = response['data']['redirect_url']
    #print("REDIRECT_URL:",hosted_url)
    return redirect(hosted_url)
