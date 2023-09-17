from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('<h1><u><i>This is from Sessions view</i></u></h1>')
def setSession(request):
    request.session['name']='Hamid Ali'
    return render(request,'sessions/setSessions.html')
def getSession(request):
    # name=request.session['name']
    name=request.session.get('name',default='Guest')
    return render(request,'sessions/getSessions.html',{"name":name})
def delSession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request,'sessions/deleteSessions.html')