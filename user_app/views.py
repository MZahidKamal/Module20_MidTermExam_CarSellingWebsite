#-----IMPORTS FROM DJANGO LIBRARY-----
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm

#-----IMPORTS FROM THIS APP-----
from .forms import UserSignup_ModelForm, UserProfileEdit_ModelForm
from purchase_app.models import Purchase_Model

#-----IMPORTS FROM OTHER APP-----

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def user_signup(request):
    if request.method == 'POST':
        form = UserSignup_ModelForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            messages.success(request, f'Welcome {user}! Your account has been created successfully!')
            return redirect('login')
    else:
        form = UserSignup_ModelForm()
    context = {'form': form, 'type': 'Sign Up'}
    return render(request, 'user_app/user_signup.html', context)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome {username}! Login successful!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
                return redirect('signup')
    else:
        form = AuthenticationForm()
    context = {'form': form, 'type': 'Login'}
    return render(request, 'user_app/user_login.html', context)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@login_required
def show_user_profile(request):
    profile = User.objects.get(username=request.user.username)
    purchases = Purchase_Model.objects.filter(user=request.user)

    # my_albums = Album_Model.objects.filter(musician=profile)
    context = {
        'first_name': profile.first_name,
        'last_name': profile.last_name,
        'email': profile.email,
        'purchases': purchases,
    }
    return render(request, 'user_app/user_profile.html', context)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@login_required
def edit_user_profile(request):
    if request.method == 'POST':
        form = UserProfileEdit_ModelForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Your profile information has been updated successfully.')
            return redirect('profile')
    else:
        form = UserProfileEdit_ModelForm(instance=request.user)
    context = {'form': form, 'type': 'Edit'}
    return render(request, 'user_app/user_edit.html', context)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@login_required
def delete_user_profile(request):
    user = request.user
    messages.success(request, f'{user.username}\'s profile information has been deleted successfully!')
    user.delete()
    return redirect('signup')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@login_required
def change_user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been updated successfully.')
            return redirect('login')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form, 'type': 'Change'}
    return render(request, 'user_app/change_password.html', context)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@login_required
def reset_user_password(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been reset successfully.')
            return redirect('login')
    else:
        form = SetPasswordForm(request.user)
    context = {'form': form, 'type': 'Reset'}
    return render(request, 'user_app/reset_password.html', context)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
