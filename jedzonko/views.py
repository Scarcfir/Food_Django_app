from datetime import datetime

from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from jedzonko.models import Plan, Recipe

from django.views.generic import ListView
from django.views import View
from django.core.paginator import Paginator
import random


class IndexView(View):

    def get(self, request):
        all_recipes = Recipe.objects.all()
        shuffle_recipes = list(all_recipes)
        random.shuffle(shuffle_recipes)
        return render(request, "index.html",
                      {'obj1': shuffle_recipes[0], 'obj2': shuffle_recipes[1], 'obj3': shuffle_recipes[2]})


class Recipes(View):
    def get(self, request):
        plan_count = Plan.objects.count()
        racipe_list = Recipe.objects.all().order_by('-votes', 'created')
        paginator = Paginator(racipe_list, 50)
        page = request.GET.get('page')
        recipes = paginator.get_page(page)
        context = {'plan_count': plan_count, 'recipes': recipes}
        return render(request, "app-recipes.html", context)


class Dashboard(View):
    def get(self, request):
        plan_count = Plan.objects.count()
        recipes_count = Recipe.objects.count()
        context = {'plan_count': plan_count, 'recipes_count': recipes_count}
        return render(request, "dashboard.html", context)


class RecipeDetails(View):
    def get(self, request, id):
        recipe_detail = Recipe.objects.get(id=id)
        ingradients = recipe_detail.ingredients.split(',')
        recipe_detail.ingredients = ingradients
        return render(request, "app-recipe-details.html", {'recipe': recipe_detail})

    def post(self, request, id):
        get_id = request.POST.get('id', None)
        recipe = Recipe.objects.get(id=get_id)
        recipe.votes += 1
        recipe.save()
        return redirect('recipe_detail',get_id)

class RecipeAdd(View):
    def get(self, request):
        return render(request, "app-add-recipe.html")

    def post(self, request):
        name = request.POST['recipe_name']
        ingredients = request.POST['ingredients']
        description = request.POST['recipe_des']
        preparation_time = request.POST['prep_time']

        if None not in [name, ingredients, description, preparation_time]:
            Recipe.objects.create(name=name, ingredients=ingredients, description=description,
                                  preparation_time=preparation_time, votes='0')
            return redirect('recipe_list')

        return render(request, "app-add-recipe.html")


class RecipeEdit(View):
    def get(self, request, id):
        if Recipe.objects.filter(id=id).exists():
            context = {}
            context['recipe'] = Recipe.objects.get(id=id)
            return render(request, "app-edit-recipe.html", context)
        return HttpResponseNotFound('<h1>Page not found</h1>')

    def post(self, request, id):
        name = request.POST['recipe_name']
        ingredients = request.POST['ingredients']
        description = request.POST['recipe_des']
        preparation_time = request.POST['prep_time']
        o = Recipe.objects.get(id=id)
        o.name = name
        o.ingredients = ingredients
        o.description = description
        o.preparation_time = preparation_time
        o.save()
        return redirect(f'/recipe/modify/{id}/')


class ScheduleDetail(View):
    def get(self, request, id):
        return render(request, "app-details-schedules.html")


class ScheduleAdd(View):
    def get(self, request):
        return render(request, "app-add-schedules.html")

    def post(self, request):
        name = request.POST.get('planName', None)
        description = request.POST.get('planDesc', None)
        if name and description:
            plan = Plan.objects.create(name=name, description=description)
            return redirect(f'/plan/{plan.id}/details')
       
        errors = "Nazwa lub opis planu jest nieprawidłowy \n"
        
        return render(request, "app-add-schedules.html", {'errors': errors})


class ScheduleAddRecepie(View):
    def get(self, request):
        return render(request, "test.html")


class ScheduleList(View):

    def get(self, request):
        page_iterator = []
        plans = Plan.objects.order_by('name')
        paginator = Paginator(plans, 50)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        for i in range(page_obj.paginator.num_pages):
            page_iterator.append(i + 1)
        return render(request, "app-schedules.html", {'plans': page_obj, 'test': page_iterator})
