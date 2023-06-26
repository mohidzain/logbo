from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Username or Password is incorrect')
        # print(username, password)
    return render(request, 'signin.html')

@login_required(login_url='/')
def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1!=password2:
            return HttpResponse('Passwords do not match')
        else:
            my_user=User.objects.create_user(username, email, password1)
            my_user.save()
            return redirect('signin')
        # return HttpResponse('User created!')
        # print(username,email,password1,password2)
    return render(request, 'signup.html')
