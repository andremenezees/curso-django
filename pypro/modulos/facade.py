from pypro.modulos.models import Modulo, Conteudo


def listar_modulos_ordenados():
    """
    Lista módulos ordenados por títulos
    :return:
    """

    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug: str) -> Modulo:
    return Modulo.objects.get(slug=slug)


def listar_conteudos_de_modulos_ordenados(modulo: Modulo):
    return list(modulo.conteudo_set.order_by('order').all())


def encontrar_conteudo(slug):
    return Conteudo.objects.select_related('modulo').get(slug=slug)


def listar_modulos_com_aulas():
    return Modulo.objects.order_by('order').all().prefetch_related('conteudo_set')
