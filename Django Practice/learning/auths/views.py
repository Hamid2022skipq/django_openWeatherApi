from django.shortcuts import render,redirect
from .forms import signup,EditUserChangeForm
from django.contrib import messages
from django.http import HttpResponse 
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm

# signup view function
def sign_up(request):
    if request.method =='POST':
        fm = signup(request.POST)
        if fm.is_valid():
            messages.success(request,'Account created Successfully!!')
            fm.save()
            return redirect('/login/') 
    else:
        fm=signup()
    return render(request,'signup.html',{'form':fm})

# login view function
def log_in(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,f'{uname} Successfully Login!!')
                    return redirect('/dashboard/')
        else:
            fm=AuthenticationForm()
        return render(request,'login.html',{'form':fm})
    else:
        return redirect('/dashboard/')    

# # from models import *
# userName="Hamid Ali"
# password1='admin'
# def signup(request):
#     pass
# def login(request):
#     name=(request.POST.get('name'))
#     password=(request.POST.get('pass'))
#     if name==userName and password1==password:
#         return redirect("dashboard/")
#     return render(request,'form.html')

# dashboard
def dashboard(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=EditUserChangeForm(request.POST,instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Profile updated Successfully!!!')
        else:
            fm=EditUserChangeForm(instance=request.user)
        return render(request,'dashboard.html',{"Name":request.user,'form':fm,})
    return redirect('/login/')

# Log_out
def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/login/')
    else:
        return redirect('/login/')


# change password with old password
def change_pass(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,f'{request.user} Successfully changed password!!')
                return redirect('/dashboard/')
        else:
            fm= PasswordChangeForm(user=request.user)
        return render(request,'changepass.html',{'form':fm})
    else:
        return redirect('/login/')
    


# change password without old password
def change_pass1(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=SetPasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,f'{request.user} Successfully changed password!!')
                return redirect('/dashboard/')
        else:
            fm= SetPasswordForm(user=request.user)
        return render(request,'changepass1.html',{'form':fm})
    else:
        return redirect('/login/')
