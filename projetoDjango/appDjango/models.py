from django.db import models

# Create your models here.
class Estoque(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=200)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return self.nome 

'''
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    categoria = models.ForeignKey(
        Estoque, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    nome_cliente = models.CharField(max_length=100)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.nome_cliente} - {self.produto.nome}'
'''