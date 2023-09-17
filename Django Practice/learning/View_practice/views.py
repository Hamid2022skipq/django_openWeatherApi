from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learndj(request):
    return HttpResponse('<h1>Hello Django Wolrd</h1>')
def learnpy(request):
    return HttpResponse('<h1>Hello python Wolrd</h1>')
