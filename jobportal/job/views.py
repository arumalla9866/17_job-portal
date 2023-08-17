from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
    return render(request,'index.html')

def admin_login(request):
    return render(request,'admin_login.html')

def user_login(request):
    error = ""
    if request.method=="POST":
        u = request.POST["uname"]
        p = request.POST["pwd"]
        user = authenticate(username=u,password=p)
        if user:
            try:
                user1 = StudentUser.objects.get(user=user)
                if user1.type == "student":
                    login(request,user)
                    error="no"
                else:
                    error = "yes"
            except:
                error = "yes"
        else:
            error = "yes"

    d = {error:"error"}


    return render(request,'user_login.html',d)

def user_signup(request):
    error = ""
    if request.method=="POST":
        f = request.POST["firstname"]
        last = request.POST["lastname"]
        con = request.POST["contact"]
        e = request.POST["email"]
        p = request.POST["pwd"]
        gen = request.POST["gender"]
        i = request.FILES["image"]
        try:
            user = User.objects.create_user(first_name=f,last_name=last,username=e,password=p)
            StudentUser.objects.create(user=user,mobile=con,image=i,gender=gen,type="student")
            error = "no"
        except:
            error = "yes"
    d = {"error":error}
    return render(request,'user_signup.html',d)


def user_home(request):
    if not request.user.is_authenticated:
        return redirect("user_login")
    return render(request,'user_home.html')
def recruiter_login(request):
    return render(request,'recruiter_login.html')