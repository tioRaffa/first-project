from django.contrib import admin
from .models import *


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email', 'idade')


class DistribuidoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'local')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Distribuidora, DistribuidoraAdmin)
