from django.shortcuts import render

# Create your views here.

from .forms import LoginForm
from django.contrib.auth import authenticate ,login
from django.http import HttpResponse

def user_login(request):
    if request.method=="POST":
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            cd=login_form.cleaned_data
            user=authenticate(username=cd['username'],password=cd['password'])
            if user:
                login(request,user)
                return  HttpResponse("Wellcome You. You have been authenticated successfully")
            else:
                return HttpResponse("Sorry, password is not right")
        else:
            return HttpResponse('invalid login')

    if request.method=="GET":
        login_form=LoginForm()
        return render(request,"registration/login.html",{"form":login_form})