from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
def members(request):
    return HttpResponse("Hello World")

def great(request):
    return HttpResponse("Hello Aliyan")
