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
    Profile
)

# Create your views here.

# ========================FOR PASSWORD RESET========================
def check_email_exists(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        user_exists = User.objects.filter(email=email).exists()

        if user_exists:
            return redirect('reset_password')
        else:
            return HttpResponse("Email does not exist!")
    return render(request, 'check_email_exists.html')


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
            user_exists = User.objects.filter(email=email).exists()
            if user_exists:
                messages.error(request, "Email is already assosiated with another account")
            else:
                password1 = request.POST.get("password1")
                password2 = request.POST.get("password2")
                if password1 != password2:
                    messages.error(request, "Passwords do not match")
                    return redirect("student_signup")
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
            user_exists = User.objects.filter(email=email).exists()
            if user_exists:
                messages.error(request, "Email is already assosiated with another account")
            else:
                password1 = request.POST.get("password1")
                password2 = request.POST.get("password2")
                if password1 != password2:
                    messages.error(request, "Passwords do not match")
                    return redirect("student_signup")
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
            user_exists = User.objects.filter(email=email).exists()
            if user_exists:
                messages.error(request, "Email is already assosiated with another account")
            else:
                password1 = request.POST.get("password1")
                password2 = request.POST.get("password2")
                if password1 != password2:
                    messages.error(request, "Passwords do not match")
                    return redirect("student_signup")
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
            user_exists = User.objects.filter(email=email).exists()
            if user_exists:
                messages.error(request, "Email is already assosiated with another account")
            else:
                password1 = request.POST.get("password1")
                password2 = request.POST.get("password2")
                if password1 != password2:
                    messages.error(request, "Passwords do not match")
                    return redirect("student_signup")
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
            user_exists = User.objects.filter(email=email).exists()
            if user_exists:
                messages.error(request, "Email is already assosiated with another account")
            else:
                password1 = request.POST.get("password1")
                password2 = request.POST.get("password2")
                if password1 != password2:
                    messages.error(request, "Passwords do not match")
                    return redirect("student_signup")
                else:
                    my_user = User.objects.create_user(username, email, password1)
                    my_user.save()
                    my_user.groups.add(admin_group)
            return redirect("admin_signin")
        except IntegrityError as e:
            messages.error(request, "Username already taken!")
    return render(request, "admin_signup.html")


# ========================LOGOUT========================
@login_required(login_url="/")
def logout_view(request):
    logout(request)
    return redirect("/")


# ========================STEPS========================
@login_required(login_url="/")
def step_1(request):
    return render(request, "step_1.html")

@login_required(login_url="/")
def step_2(request):
    return render(request, "step_2.html")

@login_required(login_url="/")
def step_3(request):
    return render(request, "step_3.html")

@login_required(login_url="/")
def step_4(request):
    return render(request, "step_4.html")

@login_required(login_url="/")
def step_5(request):
    return render(request, "step_5.html")

@login_required(login_url="/")
def step_6(request):
    return render(request, "step_6.html")

@login_required(login_url="/")
def step_7(request):
    return render(request, "step_7.html")

@login_required(login_url="/")
def step_8(request):
    return render(request, "step_8.html")

@login_required(login_url="/")
def survey(request):
    return render(request, "survey.html")

@login_required(login_url="/")
def logbook_complete(request):
    return render(request, "logbook_complete.html")

# ========================STEPS========================
@login_required(login_url="/")
def team_portal(request):
    return render(request, "team_portal.html")

@login_required(login_url="/")
def view_team(request):
    return render(request, "view_team.html")

from .forms import UpdateUserForm, UpdateProfileForm

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        # profile_form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {'user_form': user_form})

# , 'profile_form': profile_form

# from django.urls import reverse_lazy
# from django.contrib.auth.views import PasswordChangeView
# from django.contrib.messages.views import SuccessMessageMixin

# class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
#     template_name = 'users/change_password.html'
#     success_message = "Successfully Changed Your Password"
#     success_url = reverse_lazy('users-home')