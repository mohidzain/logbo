from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

# ===============FOR STUDENTS===============
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

@login_required(login_url='/')
def student_portal(request):
    return render(request, 'student_portal.html')


# ===============FOR TEACHERS===============
def teacher_signup(request):
    return render(request, 'teacher_signup.html')





# SIGN UP
def judge_signup(request):
    return render(request, 'judge_signup.html')

def mentor_signup(request):
    return render(request, 'mentor_signup.html')

def admin_signup(request):
    return render(request, 'admin_signup.html')



# LOGIN
def judge_signin(request):
    return render(request, 'judge_signin.html')

def mentor_signin(request):
    return render(request, 'mentor_signin.html')

def admin_signin(request):
    return render(request, 'admin_signin.html')

def teacher_signin(request):
    return render(request, 'teacher_signin.html')

def logout_view(request):
    logout(request)
    return redirect('/')