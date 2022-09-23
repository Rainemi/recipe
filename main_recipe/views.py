from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe
# Create your views here.

def home(request):
    recipe = Recipe.objects.all()
    context = { 
        'recipes': recipe
    }
    return render(request,'main_recipe/index.html',context)

def about(request):
    """
    recipe = Recipe.objects.all()
    context = { 
        'recipes': recipe
    }"""
    return render(request,'main_recipe/about.html')

#def layout(request):
    #return render(request,'main_recipe/layout.html')


