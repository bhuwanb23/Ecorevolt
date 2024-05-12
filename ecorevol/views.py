from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request,'login.html')

def partner(request):
    return render(request,'partner.html')

def profile(request):
    return render(request,'profile.html')

def projects(request):
    return render(request,'projects.html')

