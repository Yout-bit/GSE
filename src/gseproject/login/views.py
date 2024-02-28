from django.shortcuts import render
from django.http import HttpResponse

def landing(request):
    return render(request, 'landing.html')

def hello(request):
    return HttpResponse("Hello, World!")

def loginSuccess(request):
    return HttpResponse("Login Successful!")