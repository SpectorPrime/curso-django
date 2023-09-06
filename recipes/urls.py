from django.urls import path
from . import views

# recipes:recipe
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),   # home
    path('recipes/<int:id>/', views.recipes, name="recipe")
    
]
