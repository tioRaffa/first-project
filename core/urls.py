from django.urls import path
from .views import index, contato, index2, produto


urlpatterns = [
    path('', index, name='home'),
    path('contato', contato),
    path('index2', index2, name='produtos'),
    path('produto/<int:id>', produto, name='produto')
]
