from atexit import register
from email import message
import email
from django.shortcuts import redirect, render
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import MyUserForm
from django.shortcuts import get_object_or_404
from .forms import MyUserForm
from datetime import datetime




@login_required
def user_logout(request):
    logout(request)
    return redirect('todo')


@login_required
def profile(request):
    return render(request,'./user/profile.html')


def user_login(request):
    username=''
    message='登入'
    username=request.POST.get('username')
    password=request.POST.get('password')
    if request.method=='POST':
        if request.POST.get('login'):

            if request.POST.get('username')=='' or request.POST.get('password')=='':
                message='帳號或密碼不能為空'
            else:
                user=authenticate(request,username=username,password=password)
                if user is None:
                    if User.objects.filter(username=username):
                        message='密碼有誤!'
                    else:
                        message='帳號有誤!'                
                else:
                    login(request,user)
                    message='登入中...'
                    return redirect('todo')

            
            
            
        if request.POST.get('register'):
            return redirect('register')
    return render(request,'./user/login.html',{'message':message,'username':username})
# Create your views here.
def user_register(request):
    
    form=MyUserForm()
    message=''
   
    if request.method=='GET':
        print('GET')
    elif request.method=='POST':
        print('POST')
        print(request.POST)
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        email=request.POST.get('email')
        
        if len(password1)<8:
            message='密碼少於8個字元'
        elif password1!=password2:
            message='兩次密碼不同!'
        else:
            if User.objects.filter(username=username).exists():
                message='帳號重複'
            else:
                user=User.objects.create_user(username=username,password=password1,email=email)
                user.save()

                message='註冊成功!'
                login(request,user)
                
                return redirect('profile')
                

            
            
        #註冊功能
        # 檢查密碼是否相同
        # 密碼不能少於8個字
        # 使用者名稱不能重複
        # 進行註冊

    return render(request,'./user/register.html',{'form':form,'message':message})