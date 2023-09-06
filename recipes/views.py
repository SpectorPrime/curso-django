from django.shortcuts import render
from utils.recipes.factory import make_recipe

# Essa view coleta request e retorna o html "home" do site
# No context, ele chama a função criada em factory.py faz um laço 
# para gerar 6 receitas


def home(request):
    return render(request, 'recipes/pages/home.html',
                  context={'recipes': [make_recipe() for _ in range(9)]})


# Essa view coleta o id de cada receita e retorna a página html
# que destaca a receita
def recipes(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True
        })
