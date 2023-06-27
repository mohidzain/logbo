from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from .models import student_group, teacher_group, judge_group, mentor_group, admin_group
# Create your views here.

# ===============FOR STUDENTS===============
def student_signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('student_portal')
        else:
            return HttpResponse('Username or Password is incorrect')
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
            # my_user.groups.add(student_group)
            return redirect('student_signin')
    return render(request, 'student_signup.html')

@login_required(login_url='/')
def student_portal(request):
    return render(request, 'student_portal.html')

# ===============FOR TEACHERS===============
def teacher_signin(request):
    return render(request, 'teacher_signin.html')

def teacher_signup(request):
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
            # my_user.groups.add(teacher_group)
            return redirect('teacher_signin')
    return render(request, 'teacher_signup.html')

@login_required(login_url='/')
def student_portal(request):
    return render(request, 'student_portal.html')

# ===============FOR JUDGES===============
def judge_signin(request):
    return render(request, 'judge_signin.html')

def judge_signup(request):
    return render(request, 'judge_signup.html')

# ===============FOR MENTORS===============
def mentor_signin(request):
    return render(request, 'mentor_signin.html')

def mentor_signup(request):
    return render(request, 'mentor_signup.html')

# ===============FOR ADMINS===============
def admin_signin(request):
    return render(request, 'admin_signin.html')

def admin_signup(request):
    return render(request, 'admin_signup.html')


# ===============LOGOUT===============
def logout_view(request):
    logout(request)
    return redirect('/')