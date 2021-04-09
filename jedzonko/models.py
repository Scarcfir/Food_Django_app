from django.db import models


# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField(null=True)
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    preparation_time = models.IntegerField()
    votes = models.IntegerField()
    updated = models.DateTimeField(auto_now_add=True)

class Plan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    recipes = models.ManyToManyField(Recipe, through='RecipePlan')


class DayName(models.Model):
    DAY_NAME = (
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    )

    day_name = models.CharField(max_length=3, choices=DAY_NAME)
    order = models.IntegerField(unique=True)


class RecipePlan(models.Model):
    meal_name = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    order = models.IntegerField()
    day_name = models.ForeignKey(DayName, on_delete=models.CASCADE)
