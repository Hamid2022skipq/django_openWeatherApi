from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime,timedelta

# Create your views here.
def hello(request):
    return HttpResponse('<h1><u><i>This is from Cookies view</i></u></h1>')
def setcookies(request):
    response= render(request,'cookies/setcookies.html')
    # response.set_cookie('name','Hamid Ali')
    response.set_signed_cookie('name','Haid Ali',salt='nm',expires=datetime.utcnow()+timedelta(days=2))
    return response
def getcookies(request):
    # name=request.COOKIES['name']
    # name=request.COOKIES.get('name')
    # name=request.COOKIES.get('name','Guest')
    name=request.get_signed_cookie('name',salt='nm',default='Guest')
    return render(request,'cookies/getcookies.html',{'name':name})
def delcookies(request):
    response=render(request,'cookies/delete_cookies.html')
    response.delete_cookie('name')
    return response