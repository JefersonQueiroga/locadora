from django.contrib import admin
from django.urls import path
from locadora.views import minha_view_simples,index,requisicao_parametros,testando_context

urlpatterns = [
    path('hello', minha_view_simples,name='hello') ,
    path('', index,name='index') ,
    path('requisicao/<str:nome>', requisicao_parametros,name='requisicao_parametros') ,
    path('testando_contexto', testando_context,name='testando_context'),
]
