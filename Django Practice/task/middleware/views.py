from django.shortcuts import render,redirect
from .form import signup
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
# from middleware.logging_middleware import AccessLogsMiddleware

# signup view function
def sign_up(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            fm = signup(request.POST)
            if fm.is_valid():
                messages.success(request,'Account created Successfully!!')
                fm.save()
                return redirect('/login/') 
        else:
            fm=signup()
        return render(request,'signup.html',{'form':fm})
    else:
        return redirect('/dashboard/') 

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

# dashboard or profile
def dashboard(request):
    if request.user.is_authenticated:  
        # user_ip = get_client_ip_address(request),"user_ip":user_ip
        return render(request,'dashboard.html',{"Name":request.user})
    return redirect('/login/')

# Log_out
def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/login/')
    else:
        return redirect('/login/')
    
# get user ip address  
# def get_client_ip_address(request):
#     req_headers = request.META
#     x_forwarded_for_value = req_headers.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for_value:
#         ip_addr = x_forwarded_for_value.split(',')[-1].strip()
#     else:
#         ip_addr = req_headers.get('REMOTE_ADDR')
#     return ip_addr
