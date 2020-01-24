from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.http import HttpResponse
from .forms import *
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# View function of signup part or creating user
def view_signup_user(request):
    if request.method == "GET":
        return render(request, 'mobile/registration/signup.html')

    else:
        print(request.POST)
        user = User.objects.create_user(username=request.POST['input_username'], password=request.POST['input_password'], email=request.POST['input_email'])
        user.save()
        return HttpResponse('Signup successful')



# View function of login
def view_login_user(request):
    if request.method == "GET":
        return render(request, 'mobile/registration/login.html')

    else:
        print(request.POST)
        user = authenticate(username=request.POST['input_username'], password=request.POST['input_password'])
        print(user)
        if user is not None:
            login(request, user)
            return render(request, 'mobile/registration/success.html')

        else:
            return HttpResponse('Invalid Username or password')



# View function of logged in successful message
def logout_request(request):
    logout(request)
    
    return HttpResponse("Logged out successfully!")
    


















