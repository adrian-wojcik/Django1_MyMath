from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.
def logo(request):
    return HttpResponse("Calculator")


