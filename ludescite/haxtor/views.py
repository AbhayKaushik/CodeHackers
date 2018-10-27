from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpRequest,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required
#import models
from haxtor.models import Answers,Questions,Topic,UserProfile,UserProg
from haxtor.forms import RegisterForm,UserProfileForm

# Create your views here.
def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user= authenticate(username=username,password=password)
        if user: 
            if user.is_active:
                login(request,user)
                print("LOGGED IN")
                return HttpResponseRedirect(reverse('index'))
    else:
        return render(request,'haxtor/login.html',{})


@login_required
def special(request):
    return HttpResponse("You're Logged in")
def index(request):
    return render(request,"haxtor/index.html")

def UserRegister(request):
    registered=False
    form = RegisterForm
    profile_form = UserProfileForm
    if request.method == "POST":
        form= RegisterForm(data=request.POST)
        profile_form= UserProfileForm(data=request.POST)
        if form.is_valid() and profile_form.is_valid():

            user=form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user=user

            profile.save()
            
            registered=True
            return render(request,"haxtor/index.html")
        else:
            print("FORM INVALID")
    return render(request,"haxtor/register.html",{'form':form,'profile_form':profile_form,'registered':registered})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))