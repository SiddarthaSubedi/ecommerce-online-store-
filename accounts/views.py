from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required



# Create your views here.


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully! Welcome!")
            return redirect(reverse("products:homepage"))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomUserCreationForm()       
    
    context = {'form': form}    
    return render(request, 'accounts/register.html', context)


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        remember_me = request.POST.get("remember")
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            
            #handle remember me
            if  not remember_me:
                request.session.set_expiry(0)  # session expire when browser close
            messages.success(request, f"Welcome back, {user.email}!")
            return redirect(reverse("products:homepage"))
        
            messages.error(request, "Invalid email or password. Please try again.")
    
    return render(request, 'accounts/login.html')


def logout_view(request):
   logout(request)
   return redirect('accounts:loginpage')


@login_required
def home_view(request):
    return render (request, 'home.html')

