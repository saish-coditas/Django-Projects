from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learnDjango(request):
    return HttpResponse("Hello Django")

def learnPython(request):
    return HttpResponse("Hello Python")

def learn_var(request):
    a=10+10
    return HttpResponse(a)

def learn_math(request):
    a=10
    b=20
    c=a+b
    return HttpResponse(c)

def learn_html(request):
    return HttpResponse('<h1> Hi HTML </h1>')