from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.
def logo(request):
    return render(request, 'base.html')

def add(request,a, b):
    return HttpResponse(str(a + b))

def subtract(request,a, b):
    return HttpResponse(str(a - b))

def multiply(request,a, b):
    return HttpResponse(str(a * b))

def divide(request,a, b):
    return HttpResponse(str(a / b))

