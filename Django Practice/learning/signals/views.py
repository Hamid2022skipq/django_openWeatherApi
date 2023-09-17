from django.shortcuts import render,redirect
from .forms import signup
from django.contrib import messages
from django.http import HttpResponse 
def sign_up(request):
    if request.method =='POST':
        fm = signup(request.POST)
        if fm.is_valid():
            messages.success(request,'Account created Successfully!!')
            fm.save()
            
    else:
        fm=signup()
    return render(request,'signup.html',{'form':fm})











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
# def dashboard(request):
#     return render(request,'dashboard.html',{'name':userName})






