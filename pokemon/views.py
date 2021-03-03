from django.http import HttpResponse, response
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect

from .models import Pokemon


def index(request):
    pokemons = Pokemon.objects.filter(published=True)

    data = {
        'pokemons': pokemons
    }
    return render(request, 'pokemon/index.html', data)
