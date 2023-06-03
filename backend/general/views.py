from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict
from .models import *

# assigning User as our User model i.e. as User_details
User = get_user_model()

def Home(request):
    return render(request,'general/home.html')

def Login(request):
    if request.method == 'POST':
        print("Request recieved")
        username = request.POST['username']
        password = request.POST['password']

        print(f"username:{username}")

        if (request.POST['type'] == 'login'):
            new_user = authenticate(username=username,password=password)
            if new_user is not None:
                login(request,new_user)
                print("User logged in successfully")
             #getting the url
            try:
                return redirect(request.GET["next"])
            except:
                return redirect("Base:Home")
                
        if (request.POST['type'] == 'signup'):
            #Basic User details.
            email = request.POST['email']
            new_user = User.objects.create_user(username=username,email=email,password=password)
            new_user.save()
            login(request,new_user)
             #getting the url
            try:
                return redirect(request.GET["next"])
            except:
                return redirect("Base:Home")


    return render(request,'general/login.html')

def Logout(request):
    logout(request)
    return redirect("Base:Home")

def FAQ(request):
    return render(request,"general/faq.html")

def About(request):
    return render(request,'general/about.html')

def Profile(request):
  if request.user.is_anonymous:
    print("Annonymous User")
    verified = False
  else:
    uname = request.user
    username = request.user
    if uname == str(username):
      verified = True
    else:
      verified = False
    # print(f"VERIFIED:{verified}")
    # print(f"UNAME:{uname},USERNAME:{username}")
  User_det = model_to_dict(User.objects.filter(username=uname).first())
  if User_det is []:
    return render(request,'index.html')
  User_det["verified"] = verified
  # print(User_det)
  return render(request,'general/userprofile.html')