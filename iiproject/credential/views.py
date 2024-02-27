from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid password or username')

    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')






def register(request):
    if request.method=="POST":
        username=request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword=request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username has already taken")
                return redirect('login')
            else:




                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                user.save();
                messages.info(request, "user created")
        else:
            messages.info(request, "password not matched ")
            return redirect('register')

        return redirect('login')

    return render(request,'register.html')


