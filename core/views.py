from django.shortcuts import render
from .models import Produto
# Create your views here.


def index(request):
    # print(dir(request.user))
    print()
    # print(f'METODO {request.user.username}, {request.user.password}')

    return render(request, 'index.html')


def index2(request):
    produtos = Produto.objects.all()

    context = {
        'curso': 'Programacao WEB!',
        'teste': 'Django framework',
        'produto': produtos,
    }
    return render(request, 'index2.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, id):
    produto_ = Produto.objects.get(id=id)
    context = {
        'produtu': produto_
    }
    return render(request, 'produto.html', context)
