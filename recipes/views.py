from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Júnior Cavalcante',
    })


def contato(request):
    return HttpResponse('contato')


def sobre(request):
    return HttpResponse('sobre')
