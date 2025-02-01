from django.urls import path
from .views import index, contato, index2, produto


urlpatterns = [
    path('', index),
    path('contato', contato),
    path('index2', index2),
    path('produto/<int:id>', produto, name='produto')
]
