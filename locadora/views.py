from django.shortcuts import render
from django.http import HttpResponse
from locadora.models import Filme

def minha_view_simples(request):
    return HttpResponse("Olá, mundo! Esta é uma resposta simples.")

def requisicao_parametros(request, nome):
    return HttpResponse("Olá, " + nome + "! Esta é uma resposta com parâmetros.")

def index(request):
    filmes = Filme.objects.all()
    dicionario = {
        'lista': filmes
    }
    return render(request, 'locadora/index.html',dicionario)

def testando_context(request):
    dados = {
        'nome': 'José',
        'email': 'joao@gmail.com',
        'idade': 20,
        'cidade': 'São Paulo',
        'cep': '59900-000',
        'is_admin': False,
    }
    return render(request, 'locadora/testando_context.html',dados)
    

def lancamento(request):
    return render(request, 'locadora/lancamento.html')

def precos(request):
    return render(request, 'locadora/precos.html')
