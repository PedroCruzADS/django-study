from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def _home(request):
    return render(request, 'recipes/home.html')


def _contato(request):
    return HttpResponse('CONTATO')


def _sobre(request):
    return HttpResponse('SOBRE')
