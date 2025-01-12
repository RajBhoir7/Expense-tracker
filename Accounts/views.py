from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
def Sign_up(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create(first_name=first_name,
                                   last_name=last_name,
                                   username=email)
        user.set_password(password)
        user.save()
        return redirect('home') 



    return render(request,'Accounts/signup.html')

def User_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)

        if not user.exists():
            messages.warning(request,'User Not Found')
            return HttpResponseRedirect(request.path_info)
        
        user1 = authenticate(username=username,password=password)
        if user1:
            login(request,user1)
            return redirect('http://127.0.0.1:8000/')
        
        else:
            messages.warning(request,'Incorrect Password')
            return HttpResponseRedirect(request.path_info)
    return render(request,'Accounts/login.html')

def User_logout(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/')
