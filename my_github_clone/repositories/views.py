from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from .models import Repository,File,Issue,Collaborator


# Create your views here.


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        User.objects.create_user(username=username,password=password)
        return redirect('login')
    return render(request,'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('repositories')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')   


#now the views for functionality


    
    
