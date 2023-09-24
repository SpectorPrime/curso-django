from django.http import Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404
from utils.recipes.factory import make_recipe
from .models import Recipe

# Essa view coleta request e retorna o html "home" do site
# No context, ele chama a função criada em factory.py faz um laço 
# para gerar 6 receitas


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html',
                  context={'recipes': recipes})


def category(request, category_id):
    recipes = get_list_or_404(Recipe.objects.filter(
        category__id=category_id, is_published=True
        ).order_by('-id')
    )
    return render(
        request, 'recipes/pages/category.html',
        context={
            'recipes': recipes,
            'title': f'{recipes[0].category.name} - Categoria | '
            })


# Essa view coleta o id de cada receita e retorna a página html
# que destaca a receita
def recipes(request, id):

    recipe = get_object_or_404(Recipe, id=id, is_published=True)

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True
        })
