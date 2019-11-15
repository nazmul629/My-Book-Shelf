from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout

def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            userame = request.POST.get('username')
            password = request.POST.get('password')
            auth = authenticate(username=userame, password=password)
            if auth :
                login(request,auth)
                return redirect('index')

    return render(request,'author/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')