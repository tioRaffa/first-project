from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def index2(request):
    context = {
        'curso': 'Programacao WEB!',
        'teste': 'Django framework'
    }
    return render(request, 'index2.html', context)


def contato(request):
    return render(request, 'contato.html')
