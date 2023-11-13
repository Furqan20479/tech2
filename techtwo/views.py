from django.shortcuts import render,redirect
from.models import Signup,PlaceOrder
from django.contrib.auth import logout,authenticate
from django.contrib.auth import login
from .serializer import SignupSerializer
from rest_framework import generics
from .serializer import PlaceOrderSerilizer
# Create your views here.

def frount_page(request):

    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'accounts/base.html')



def signup_user(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        user = Signup(name=name, email=email, password=password, confirmpassword=confirmpassword)
        user.save()
        

    return render(request, 'accounts/signup.html')


def placeorder(request):

    if request.method == "POST":
        productname = request.POST.get('productname')
        quantity = request.POST.get('quantity')
        name = request.POST.get('name')
        adress = request.POST.get('adress')
        print(name, productname, quantity, adress)
        
        info = PlaceOrder(productname=productname, quantity=quantity, name=name, adress=adress)
        info.save()

    return render(request, 'accounts/mtemp.html')

def login_view(request):

    if request.method == "POST":

        name = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(name=name, password=password)

        if user is not None:
            login(request,user)

            return redirect("accounts/base.html")
        else:
             return render(request, 'accounts/login.html')

    return render(request, 'accounts/login.html')
        

def logout_user(request):

    logout(request)
    return redirect('/login')



class users(generics.ListCreateAPIView):

    queryset = Signup.objects.all()
    serializer_class = SignupSerializer

class items(generics.ListCreateAPIView):

    queryset = PlaceOrder.objects.all()
    serializer_class = PlaceOrderSerilizer


