from django.db import models

# Create your models here.


class Produto(models.Model):
    nome = models.CharField('nome', max_length=100)
    preco = models.DecimalField('Preo', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em Estoque')


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=50)
    sobrenome = models.CharField('Sobrenome', max_length=50)
    email = models.EmailField('E-mail', max_length=100)
    idade = models.IntegerField('Idade')
