from django.shortcuts import render
from django.http import HttpResponse


def minha_view_simples(request):
    return HttpResponse("Olá, mundo! Esta é uma resposta simples.")

def requisicao_parametros(request, nome):
    return HttpResponse("Olá, " + nome + "! Esta é uma resposta com parâmetros.")

def index(request):
    return render(request, 'locadora/index.html')