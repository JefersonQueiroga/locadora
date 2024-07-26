from django.db import models


class Genero(models.Model):
    descricao = models.CharField(max_length=100)
    
    def __str__(self):
        return self.descricao
    
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    duracao = models.IntegerField()
    ano = models.IntegerField()
    sinopse = models.TextField()
    diretor = models.CharField(max_length=100)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.titulo

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=11)
    
    def __str__(self):
        return self.nome
    
class Locacao(models.Model):
    data_locacao = models.DateField()
    data_devolucao = models.DateField()
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    filme = models.ManyToManyField(Filme)
    
    def __str__(self):
        return self.cliente.nome + ' - ' + self.filme.titulo