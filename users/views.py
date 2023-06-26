from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def student_signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('student_profile')
        else:
            return HttpResponse('Username or Password is incorrect')
        # print(username, password)
    return render(request, 'student_signin.html')

@login_required(login_url='/')
def student_profile(request):
    return render(request, 'student_profile.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def student_signup(request):
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
            return redirect('student_signin')
        # return HttpResponse('User created!')
        # print(username,email,password1,password2)
    return render(request, 'student_signup.html')

def judge_signup(request):
    pass
def mentor_signup(request):
    pass
def admin_signup(request):
    pass
