from django.urls import path
from .views import index, contato, index2


urlpatterns = {
    path('', index),
    path('contato', contato),
    path('index2', index2)
}
