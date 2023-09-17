from django.shortcuts import render,redirect,get_object_or_404
from .forms import signup,EditUserChangeForm,EditAdminChangeForm
from django.contrib import messages
from django.http import HttpResponse 
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.models import User

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




# dashboard or profile
def dashboard(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            if request.user.is_superuser == True:
                fm=EditAdminChangeForm(request.POST,instance=request.user)
                users = User.objects.all()
            else:
                fm=EditUserChangeForm(request.POST,instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Profile updated Successfully!!!')
                users=None
        else:
            if request.user.is_superuser == True:
                fm=EditAdminChangeForm(instance=request.user)
                users = User.objects.all()
            else:
                fm=EditUserChangeForm(instance=request.user)
                users=None
        return render(request,'dashboard.html',{"Name":request.user,'form':fm,'users':users})
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

def userprofile(request,id):
    if request.user.is_authenticated:
        pi = get_object_or_404(User, pk=id)
        if request.user.is_superuser == True:
            fm=EditAdminChangeForm(instance=pi)
            return render(request,'userProfile.html',{'form':fm})
        else:
            fm=EditUserChangeForm(instance=pi)
            return render(request,'userProfile.html',{'form':fm,'name':request.username})
    else:
        return redirect('/login/') 