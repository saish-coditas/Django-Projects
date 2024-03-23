from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def admindj(request):
    return HttpResponse("Admin Django")

def adminpy(request):
    return HttpResponse("Admin Python")

def adminhtml(request):
    return HttpResponse("Admin HTML")

def adminString(request):
    return HttpResponse("Admin String")
