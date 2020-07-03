from django.shortcuts import render

from requests import request


def indice(request):
    return render(request, 'turmas/indice.html')
