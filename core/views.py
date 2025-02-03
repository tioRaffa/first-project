from django.shortcuts import render
from .models import Produto

from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.template import loader
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
    # produto_ = Produto.objects.get(id=id)

    produto_ = get_object_or_404(Produto, id=id)
    context = {
        'produtu': produto_
    }
    return render(request, 'produto.html', context)


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8', status=500)
