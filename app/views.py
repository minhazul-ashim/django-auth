from django.shortcuts import render

# Create your views here.
def register(request) :
    return render(request, 'register.html');

def login(request) :
    return render(request, 'login.html');

def profile(request) :
    return render(request, 'profile.html');