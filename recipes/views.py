from django.shortcuts import render


# Essa view coleta request e retorna o html "home" do site #
def home(request):
    return render(request, 'recipes/pages/home.html',
                  context={'name': 'Rodrigo'})


# Essa view coleta o id de cada receita e retorna a página html
# que destaca a receita
def recipes(request, id):
    return render(request, 'recipes/pages/recipe-view.html',
                  context={'name': 'Rodrigo'})
