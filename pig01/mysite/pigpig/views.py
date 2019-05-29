from django.shortcuts import render
from pigpig.models import Taste, Cooking, Recipe
# Create your views here.

def pigpig(request):

    return render(request, 'pigpig/index.html')

def indexCut(request):

    return render(request, 'pigpig/index-cut.html')

def inner(request):

    tastes = Taste.objects.all()
    cookings = Cooking.objects.all()
    recipes = Recipe.objects.all()
    context = {'tastes':tastes, 'cookings':cookings, 'recipes':recipes}
    return render(request, 'pigpig/inner.html', context)