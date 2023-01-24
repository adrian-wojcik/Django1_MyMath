from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.
def logo(request):
    return HttpResponse("Calculator")


def add(reuest,a, b):
    return HttpResponse(sum(a, b))
