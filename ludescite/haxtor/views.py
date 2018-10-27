from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpRequest,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required
#import models
from haxtor.models import Answers,Questions,Topic,UserProfile,UserProg
from haxtor.forms import RegisterForm,UserProfileForm


def about(request):
    return render(request,"haxtor/about.html")
def contact(request):
    return render(request,"haxtor/contact.html")
def legal(request):
    return render(request,"haxtor/legal.html")

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
                userData = UserProfile.objects.get(user=request.user)
                print(userData)
                return render(request,'haxtor/dashboard.html',{"userdata":userData})
        else:
            
            print("Someone tried to login and failed !")
            print("Username : {} and password {} ".format(username,password))
            return HttpResponse("Invalid login details supplied !")
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
        print("FLAG 0")
        if form.is_valid() and profile_form.is_valid():

            user=form.save()
            user.set_password(user.password)
            user.save()
            print("FLAG 1")
            profile = profile_form.save(commit=False)
            profile.user=user
            print("FLAG 2")
            profile.save()
            print("FLAG 3")
            registered=True
            return render(request,"haxtor/index.html")
        else:
            print("FORM INVALID")
    return render(request,"haxtor/register.html",{'form':form,'profile_form':profile_form,'registered':registered})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def user_dashboard(request):
    userData = UserProfile.objects.get(user=request.user)
    return render(request,"haxtor/dashboard.html",{"userdata":userData})

def userQuestions(request):
    levels=("1","2")
    from random import choice
    ext=choice(levels)
    id=IDextract(ext)
    ques=Questions.objects.get(quesID=id)
    while ques.quesImg:
        id=IDextract(ext)
        ques=Questions.objects.get(quesID=id)
    ansData = Answers.objects.filter(quesID=id)
    # if request.method=="POST":
    #     ID=request.POST("group1")
    #     print(ID)

    
    return render(request,"haxtor/question.html",{"ques":ques,"ansData":ansData})
    # quesList = list(i.quesText for i in quesData)


def IDextract(level):
    quesData = Questions.objects.filter(quesLevel=level)
    quesList = list(i.quesID for i in quesData)
    from random import choice
    quesID= choice(quesList)
    return quesID

def submitAnswer(request):
    if request.method=="POST":
        ID=request.POST["group1"]
        ansObject=Answers.objects.get(ansID=ID)
        
        #Answer is correct
        if ansObject.ansCorrect:
            print("ANSWER was Correct")
            user=UserProfile.objects.get(user=request.user)
            point=user.point
            print(user)
            print(point)
            UserProfile.objects.filter(user=request.user).update(point=point+2)
            for i in UserProfile.objects.filter(user=request.user):
                i.save()
            return HttpResponseRedirect(reverse("haxtor:testQuestions"))
            # quesUsedID=ansObject.quesID
            # id=IDextract("2",quesUsedID)
            # print(id)
            # ques=Questions.objects.get(quesID=id)
            # ansData = Answers.objects.filter(quesID=id).all()
            # print(ansData)
            # return render(request,"haxtor/question.html",{"ques":ques,"ansData":ansData})
        
        else:
            print("ANSWER was WRONG")
            return HttpResponseRedirect(reverse("haxtor:testQuestions"))