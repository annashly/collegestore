# Create your views here.
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        users=auth.authenticate(username=username, password=password)
        if users is not None:
            auth.login(request,users)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return  redirect('register')
        return redirect('/')
    return render(request, "register.html")



