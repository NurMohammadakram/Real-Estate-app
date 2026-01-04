from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .models import Profile
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'auth/profile.html')

def user_register(request):
    if request.method == "POST":
        user = User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password'],
        )
        Profile.objects.create(
            user=user,
            role=request.POST.get('role', 'user')
        )
        login(request, user)
        return redirect('profile')
    return render(request, 'auth/register.html')


def user_login(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('profile')
    return render(request, 'auth/login.html')

def user_logout(request):
    
    logout(request)
    return redirect('home')

@login_required
def change_password(request):
    user = request.user
    
    if request.method == "POST":
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        
        if not user.check_password(old_password):
            messages.error(request, "Invalid Credentials")
            return redirect('change_password')
        if new_password != confirm_password:
            messages.error(request, 'new password did not match confirm password')
            return redirect('change_password')
        
        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)
        messages.success(request, 'Password updated succesfully')
        return redirect('profile')
    return render(request, 'auth/change_password.html')
    
