from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from .models import (
    student_group,
    teacher_group,
    judge_group,
    mentor_group,
    admin_group,
    Student,
)

# Create your views here.


def step_1(request):
    return render(request, "step_1.html")


def step_2(request):
    return render(request, "step_2.html")


def step_3(request):
    return render(request, "step_3.html")


def step_4(request):
    return render(request, "step_4.html")


def step_5(request):
    return render(request, "step_5.html")


def step_6(request):
    return render(request, "step_6.html")


def step_7(request):
    return render(request, "step_7.html")


def step_8(request):
    return render(request, "step_8.html")


def team_portal(request):
    return render(request, "team_portal.html")


def view_team(request):
    return render(request, "view_team.html")


def survey(request):
    return render(request, "survey.html")


def logbook_complete(request):
    return render(request, "logbook_complete.html")


# ========================FOR STUDENTS========================
def student_signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("student_portal")
        else:
            messages.error(request, "Username or Password is incorrect!")
    return render(request, "student_signin.html")


def student_signup(request):
    if request.method == "POST":
        try:
            username = request.POST.get("username")
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            if password1 != password2:
                messages.error(request, "Passwords do not match")
            else:
                my_user = User.objects.create_user(username, email, password1)
                my_user.save()
                my_user.groups.add(student_group)
            return redirect("student_signin")
        except IntegrityError as e:
            messages.error(request, "Username already taken!")
    return render(request, "student_signup.html")


@login_required(login_url="/")
def student_portal(request):
    # if 'first_login' not in request.session:
    #     request.session['first_login'] = True
    #     # Additional logic for first-time login
    # else:
    #     request.session['first_login'] = False
    #     # Additional logic for subsequent logins
    return render(request, "student_portal.html")


@login_required(login_url="/")
def student_profile(request):
    if request.method == "POST":
        f_name = request.POST.get("f_name")
        l_name = request.POST.get("l_name")
        excited = request.POST.get("excited")
        time = request.POST.get("time")
        book = request.POST.get("book")
        food = request.POST.get("food")
        student = Student(
            f_name=f_name,
            l_name=l_name,
            excited=excited,
            time=time,
            book=book,
            food=food,
        )
        student.save()
        messages.success(request, "Profile Saved!")
        return redirect("student_portal")
    return render(request, "student_profile.html")


@login_required(login_url="/")
def profile_edit(request):
    if request.method == "POST":
        try:
            username = request.POST.get("username")
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            if password1 != password2:
                messages.error(request, "Passwords do not match")
            else:
                my_user = User.objects.create_user(username, email, password1)
                my_user.save()
                my_user.groups.add(student_group)
            return redirect("student_signin")
        except IntegrityError as e:
            messages.error(request, "Username already taken!")
    return render(request, "student_profile.html")


# ========================FOR TEACHERS========================
def teacher_signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("teacher_profile")
        else:
            print("Done")
            messages.error(request, "Username or Password is incorrect!")
    return render(request, "teacher_signin.html")


def teacher_signup(request):
    if request.method == "POST":
        try:
            username = request.POST.get("username")
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            if password1 != password2:
                messages.error(request, "Passwords do not match")
            else:
                my_user = User.objects.create_user(username, email, password1)
                my_user.save()
                my_user.groups.add(teacher_group)
            return redirect("teacher_signin")
        except IntegrityError as e:
            messages.error(request, "Username already taken!")
    return render(request, "teacher_signup.html")


@login_required(login_url="/")
def teacher_profile(request):
    return render(request, "teacher_profile.html")


# ========================FOR JUDGES========================
def judge_signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("student_portal")
        else:
            messages.error(request, "Username or Password is incorrect!")
    return render(request, "judge_signin.html")


def judge_signup(request):
    if request.method == "POST":
        try:
            username = request.POST.get("username")
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            if password1 != password2:
                messages.error(request, "Passwords do not match")
            else:
                my_user = User.objects.create_user(username, email, password1)
                my_user.save()
                my_user.groups.add(judge_group)
            return redirect("judge_signin")
        except IntegrityError as e:
            messages.error(request, "Username already taken!")
    return render(request, "judge_signup.html")


# ========================FOR MENTORS========================
def mentor_signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("student_portal")
        else:
            messages.error(request, "Username or Password is incorrect!")
    return render(request, "mentor_signin.html")


def mentor_signup(request):
    if request.method == "POST":
        try:
            username = request.POST.get("username")
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            if password1 != password2:
                messages.error(request, "Passwords do not match")
            else:
                my_user = User.objects.create_user(username, email, password1)
                my_user.save()
                my_user.groups.add(mentor_group)
            return redirect("mentor_signin")
        except IntegrityError as e:
            messages.error(request, "Username already taken!")
    return render(request, "mentor_signup.html")


# ========================FOR ADMINS========================
def admin_signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("student_portal")
        else:
            messages.error(request, "Username or Password is incorrect!")
    return render(request, "admin_signin.html")


def admin_signup(request):
    if request.method == "POST":
        try:
            username = request.POST.get("username")
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            if password1 != password2:
                messages.error(request, "Passwords do not match")
            else:
                my_user = User.objects.create_user(username, email, password1)
                my_user.save()
                my_user.groups.add(admin_group)
            return redirect("admin_signin")
        except IntegrityError as e:
            messages.error(request, "Username already taken!")
    return render(request, "admin_signup.html")


# ========================LOGOUT========================
def logout_view(request):
    logout(request)
    return redirect("/")
