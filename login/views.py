from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm
from datetime import date



# Create your views here.
# Home page
def index(request):
    today = date.today()
    day_name = today.strftime("%A") + " " + today.strftime('%d/%B/%Y')   
    # day_name = today.strftime("%A") + " " + str(today)
    return render(request, 'login/index.html', {'day': day_name})

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'login/signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')