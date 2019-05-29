from django.shortcuts import render
from pigpig.models import Taste, Cooking, Recipe
# Create your views here.

def pigpig(request):

    return render(request, 'pigpig/index.html')

def indexCut(request):

    return render(request, 'pigpig/index-cut.html')

def a(request):

    tastes = Taste.objects.all()
    cookings = Cooking.objects.all()
    recipes = Recipe.objects.all()
    context = {'tastes':tastes, 'cookings':cookings, 'recipes':recipes}
    return render(request, 'pigpig/a.html', context)

def b(request):

    tastes = Taste.objects.all()
    cookings = Cooking.objects.all()
    recipes = Recipe.objects.all()
    context = {'tastes':tastes, 'cookings':cookings, 'recipes':recipes}
    return render(request, 'pigpig/b.html', context)
def c(request):

    tastes = Taste.objects.all()
    cookings = Cooking.objects.all()
    recipes = Recipe.objects.all()
    context = {'tastes':tastes, 'cookings':cookings, 'recipes':recipes}
    return render(request, 'pigpig/c.html', context)
def d(request):

    tastes = Taste.objects.all()
    cookings = Cooking.objects.all()
    recipes = Recipe.objects.all()
    context = {'tastes':tastes, 'cookings':cookings, 'recipes':recipes}
    return render(request, 'pigpig/d.html', context)
def e(request):

    tastes = Taste.objects.all()
    cookings = Cooking.objects.all()
    recipes = Recipe.objects.all()
    context = {'tastes':tastes, 'cookings':cookings, 'recipes':recipes}
    return render(request, 'pigpig/e.html', context)
def f(request):

    tastes = Taste.objects.all()
    cookings = Cooking.objects.all()
    recipes = Recipe.objects.all()
    context = {'tastes':tastes, 'cookings':cookings, 'recipes':recipes}
    return render(request, 'pigpig/f.html', context)
def g(request):

    tastes = Taste.objects.all()
    cookings = Cooking.objects.all()
    recipes = Recipe.objects.all()
    context = {'tastes':tastes, 'cookings':cookings, 'recipes':recipes}
    return render(request, 'pigpig/g.html', context)
def h(request):

    tastes = Taste.objects.all()
    cookings = Cooking.objects.all()
    recipes = Recipe.objects.all()
    context = {'tastes':tastes, 'cookings':cookings, 'recipes':recipes}
    return render(request, 'pigpig/h.html', context)
def i(request):

    tastes = Taste.objects.all()
    cookings = Cooking.objects.all()
    recipes = Recipe.objects.all()
    context = {'tastes':tastes, 'cookings':cookings, 'recipes':recipes}
    return render(request, 'pigpig/i.html', context)
def j(request):

    tastes = Taste.objects.all()
    cookings = Cooking.objects.all()
    recipes = Recipe.objects.all()
    context = {'tastes':tastes, 'cookings':cookings, 'recipes':recipes}
    return render(request, 'pigpig/j.html', context)
def k(request):

    tastes = Taste.objects.all()
    cookings = Cooking.objects.all()
    recipes = Recipe.objects.all()
    context = {'tastes':tastes, 'cookings':cookings, 'recipes':recipes}
    return render(request, 'pigpig/k.html', context)
