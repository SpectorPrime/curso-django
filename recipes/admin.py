from django.contrib import admin
from .models import Category, Recipe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...


# admin.site.register(Category, CategoryAdmin) -> É outra forma de registrar a model no admin
