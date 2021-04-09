"""scrumlab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
1. Add an import:  from my_app import views
2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
1. Add an import:  from other_app.views import Home
2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
1. Import the include() function: from django.urls import include, path
2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from jedzonko.views import IndexView, Recipes, Dashboard, RecipeAdd, RecipeEdit, RecipeDetails, \
    ScheduleAddRecepie, ScheduleDetail, ScheduleAdd, ScheduleList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('main/', Dashboard.as_view(), name="dashboard"),
    path('recipe/<int:id>/', RecipeDetails.as_view(), name='recipe_detail'),
    path('recipe/list/', Recipes.as_view(), name='recipe_list'),
    path('recipe/add/', RecipeAdd.as_view(), name='recipe_add'),
    path('recipe/modify/<int:id>/', RecipeEdit.as_view(), name='recipe_edit'),
    path('plan/<int:id>/', ScheduleDetail.as_view(), name='schedule_detail'),
    path('plan/add/', ScheduleAdd.as_view(), name='schedule_add'),
    path('plan/add-receipe/', ScheduleAddRecepie.as_view(), name='schedule_add_recipe'),
    path('plan/list/', ScheduleList.as_view(), name='schedule_list')
]
