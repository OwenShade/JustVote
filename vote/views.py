from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home.html')

def search(request):
    return render(request, 'search.html')

def browse(request):
    return render(request, 'browse.html')

def profile(request):
    return render(request, 'profile.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')