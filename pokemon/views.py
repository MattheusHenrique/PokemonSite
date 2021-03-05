from django.http import HttpResponse, response
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect

from .models import Pokemon


def index(request):
    pokemons = Pokemon.objects.filter(published=True)

    data = {
        'pokemons': pokemons
    }
    return render(request, 'pokemon/index.html', data)

def search(request):
    list_pokemons = Pokemon.objects.filter(published=True)

    if 'search' in request.GET:
        name_search = request.GET['search']
        if search:
            list_pokemons = list_pokemons.filter(name__icontains=name_search)

    data = {
        'pokemons': list_pokemons
    }

    return render(request, 'pokemon/search.html', data)


