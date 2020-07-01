from django.shortcuts import render

from pypro.modulos import facade


def detalhe(request, slug):
    modulo = facade.encontrar_modulo(slug)
    conteudos = facade.listar_conteudos_de_modulos_ordenados(modulo)
    return render(request, 'modulos/modulo_detalhe.html', {'modulo': modulo, 'conteudos': conteudos})
