from django.shortcuts import render
from http.client import HTTPResponse
from django.http import HttpResponse
# Create your views here.

def user(request):
    return render(request,'user/index.html')
