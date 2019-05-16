from django.shortcuts import render

# Create your views here.

from django.contrib.auth import authenticate ,login
from django.http import HttpResponse
from .forms import LoginForm,RegistrationForm
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

def register(request):
    if request.method=="POST":
        user_form=RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return HttpResponse('successfully')
        else:
            return HttpResponse("sorry, you can not register")
    else:
        user_form=RegistrationForm()
        return render(request,"account/register.html",{"form":user_form})