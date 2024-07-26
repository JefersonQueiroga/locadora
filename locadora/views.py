from django.shortcuts import render
from django.http import HttpResponse
from locadora.models import Filme

def minha_view_simples(request):
    return HttpResponse("Olá, mundo! Esta é uma resposta simples.")

def requisicao_parametros(request, nome):
    return HttpResponse("Olá, " + nome + "! Esta é uma resposta com parâmetros.")

def index(request):
    filmes = Filme.objects.all()
    context = {
        'filmes': filmes
    }
    return render(request, 'locadora/index.html',context)

def testando_context(request):
    context = {
        'nome': 'João',
        'idade': 30,
        'cidade': 'São Paulo',
        'is_admin': False,
    }
    return render(request, 'locadora/testando_context.html',context)