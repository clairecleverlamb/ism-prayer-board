from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomSignupForm, CustomSigninForm
import re

ALLOWED_EMAIL_DOMAIN = "acts2.network"
ADMIN_EMAILS = ["claire.chen@acts2.network", "shufei.lei@acts2.network", "karen.lei@acts2.network"]

#signup View
ALLOWED_EMAIL_DOMAIN = "acts2.network"

def signup_view(request):
    if request.method == "POST":
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user.email in ADMIN_EMAILS:
                user.is_staff = True
                user.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomSignupForm()
    return render(request, "auth/signup.html", {"form": form})

# Signin View
def signin_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "auth/signin.html", {"form": form})

# Signout View
@login_required
def signout_view(request):
    logout(request)
    return redirect("signin")

