from django.contrib import admin
from .models import Pokemon

class listPokemon(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'published')
    list_display_links = ('id', 'name')
    list_filter = ('type', )
    list_editable = ('published', )
    list_per_page = 5


admin.site.register(Pokemon, listPokemon)
