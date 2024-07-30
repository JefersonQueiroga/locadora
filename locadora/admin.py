from django.contrib import admin
from .models import Genero, Filme, Cliente, Locacao

@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'duracao', 'ano', 'diretor', 'genero')
    list_filter = ('genero', 'ano')
    search_fields = ('titulo', 'diretor')


admin.site.register(Genero)