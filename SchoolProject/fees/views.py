from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def feesdj(request):
    return HttpResponse("Fees Django")

def feespy(request):
    return HttpResponse("Fees Python")

def feeshtml(request):
    return HttpResponse("Fees HTML")

def feesString(request):
    return HttpResponse("Fees String")