from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from pypro.modulos import facade


def indice(request):
    ctx = {'modulos': facade.listar_modulos_com_aulas()}
    return render(request, 'modulos/indice.html', ctx)


def detalhe(request, slug):
    modulo = facade.encontrar_modulo(slug)
    conteudos = facade.listar_conteudos_de_modulos_ordenados(modulo)
    return render(request, 'modulos/modulo_detalhe.html', {'modulo': modulo, 'conteudos': conteudos})


@login_required
def conteudo(request, slug):
    conteudo = facade.encontrar_conteudo(slug)
    return render(request, 'modulos/conteudo_detalhe.html', {'conteudo': conteudo})
