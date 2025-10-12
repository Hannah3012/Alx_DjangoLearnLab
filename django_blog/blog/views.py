from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import Profile
from django.contrib.auth.models import User

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in the user after registration
            messages.success(request, "Registration successful!")
            return redirect('profile')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        if email:
            request.user.email = email
            request.user.save()
        profile.bio = bio
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']
        profile.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('profile')
    return render(request, 'blog/profile.html', {'profile': profile})
