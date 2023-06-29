from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from .models import student_group, teacher_group, judge_group, mentor_group, admin_group
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
            messages.error(request, 'Username or Password is incorrect!')
    return render(request, 'student_signin.html')

def student_signup(request):
    if request.method=='POST':
        try:
            username=request.POST.get('username')
            email=request.POST.get('email')
            password1=request.POST.get('password1')
            password2=request.POST.get('password2')
            if password1!=password2:
                messages.error(request, 'Passwords do not match')
            else:
                my_user=User.objects.create_user(username, email, password1)
                my_user.save()
                my_user.groups.add(student_group)
            return redirect('student_signin')
        except IntegrityError as e:
            messages.error(request, 'Username already taken!')
    return render(request, 'student_signup.html')

@login_required(login_url='/')
def student_portal(request):
    return render(request, 'student_portal.html')

@login_required(login_url='/')
def student_profile(request):
    return render(request, 'student_profile.html')

@login_required(login_url='/')
def profile_edit(request):
    if request.method=='POST':
        try:
            username=request.POST.get('username')
            email=request.POST.get('email')
            password1=request.POST.get('password1')
            password2=request.POST.get('password2')
            if password1!=password2:
                messages.error(request, 'Passwords do not match')
            else:
                my_user=User.objects.create_user(username, email, password1)
                my_user.save()
                my_user.groups.add(student_group)
            return redirect('student_signin')
        except IntegrityError as e:
            messages.error(request, 'Username already taken!')
    return render(request, 'student_profile.html')

# ===============FOR TEACHERS===============
def teacher_signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('teacher_profile')
        else:
            print('Done')
            messages.error(request, 'Username or Password is incorrect!')
    return render(request, 'teacher_signin.html')

def teacher_signup(request):
    if request.method=='POST':
        try:
            username=request.POST.get('username')
            email=request.POST.get('email')
            password1=request.POST.get('password1')
            password2=request.POST.get('password2')
            if password1!=password2:
                messages.error(request, 'Passwords do not match')
            else:
                my_user=User.objects.create_user(username, email, password1)
                my_user.save()
                my_user.groups.add(teacher_group)
            return redirect('teacher_signin')
        except IntegrityError as e:
            messages.error(request, 'Username already taken!')
    return render(request, 'teacher_signup.html')

@login_required(login_url='/')
def teacher_profile(request):
    return render(request, 'teacher_profile.html')

# @login_required(login_url='/')
# def landing(request):
#     return HttpResponse('Student')

# ===============FOR JUDGES===============
def judge_signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('student_portal')
        else:
            messages.error(request, 'Username or Password is incorrect!')
    return render(request, 'judge_signin.html')

def judge_signup(request):
    if request.method=='POST':
        try:
            username=request.POST.get('username')
            email=request.POST.get('email')
            password1=request.POST.get('password1')
            password2=request.POST.get('password2')
            if password1!=password2:
                messages.error(request, 'Passwords do not match')
            else:
                my_user=User.objects.create_user(username, email, password1)
                my_user.save()
                my_user.groups.add(judge_group)
            return redirect('judge_signin')
        except IntegrityError as e:
            messages.error(request, 'Username already taken!')
    return render(request, 'judge_signup.html')

# ===============FOR MENTORS===============
def mentor_signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('student_portal')
        else:
            messages.error(request, 'Username or Password is incorrect!')
    return render(request, 'mentor_signin.html')

def mentor_signup(request):
    if request.method=='POST':
        try:
            username=request.POST.get('username')
            email=request.POST.get('email')
            password1=request.POST.get('password1')
            password2=request.POST.get('password2')
            if password1!=password2:
                messages.error(request, 'Passwords do not match')
            else:
                my_user=User.objects.create_user(username, email, password1)
                my_user.save()
                my_user.groups.add(mentor_group)
            return redirect('mentor_signin')
        except IntegrityError as e:
            messages.error(request, 'Username already taken!')
    return render(request, 'mentor_signup.html')

# ===============FOR ADMINS===============
def admin_signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('student_portal')
        else:
            messages.error(request, 'Username or Password is incorrect!')
    return render(request, 'admin_signin.html')

def admin_signup(request):
    if request.method=='POST':
        try:
            username=request.POST.get('username')
            email=request.POST.get('email')
            password1=request.POST.get('password1')
            password2=request.POST.get('password2')
            if password1!=password2:
                messages.error(request, 'Passwords do not match')
            else:
                my_user=User.objects.create_user(username, email, password1)
                my_user.save()
                my_user.groups.add(admin_group)
            return redirect('admin_signin')
        except IntegrityError as e:
            messages.error(request, 'Username already taken!')
    return render(request, 'admin_signup.html')


# ===============LOGOUT===============
def logout_view(request):
    logout(request)
    return redirect('/')

 