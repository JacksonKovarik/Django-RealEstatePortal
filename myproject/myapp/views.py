from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Hey, Welcome</h1>')

def sell(request):
    return HttpResponse('<h1>Hey, Welcome Sell</h1>')

def rent(request):
    pass

def signIn(request):
    pass

def signUp(request):
    pass
