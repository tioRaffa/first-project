from django.db import models

# Create your models here.


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preco', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em Estoque')

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=50)
    sobrenome = models.CharField('Sobrenome', max_length=50)
    email = models.EmailField('E-mail', max_length=100)
    idade = models.IntegerField('Idade')

    def __str__(self):
        return f'{self.nome} {self.sobrenome} - {self.idade}'


class Distribuidora(models.Model):
    nome = models.CharField('Nome', max_length=50)
    cnpj = models.CharField('CNPJ', max_length=18, unique=True)
    local = models.CharField('Local', max_length=100)

    def __str__(self):
        return self.nome
