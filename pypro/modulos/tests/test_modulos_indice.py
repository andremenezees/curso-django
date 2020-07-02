import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.django_assertions import assert_contains
from pypro.modulos.models import Modulo, Conteudo


@pytest.fixture
def modulos(db):
    return mommy.make(Modulo, 2)


@pytest.fixture
def conteudos(modulos):
    conteudos = []
    for modulo in modulos:
        conteudos.extend(mommy.make(Conteudo, 3, modulo=modulo))
    return conteudos


@pytest.fixture
def resp(client, modulos, conteudos):
    resp = client.get(reverse('modulos:indice'))
    return resp


def test_indice_disponivel(resp):
    assert resp.status_code == 200


def test_titulos(resp, modulos: Modulo):
    for modulo in modulos:
        assert_contains(resp, modulo.titulo)


def test_descricao(resp, modulos: Modulo):
    for modulo in modulos:
        assert_contains(resp, modulo.descricao)


def test_publico(resp, modulos: Modulo):
    for modulo in modulos:
        assert_contains(resp, modulo.publico)


def test_conteudos_titulos(resp, conteudos: Conteudo):
    for conteudo in conteudos:
        assert_contains(resp, conteudo.titulo)


def test_conteudos_urls(resp, conteudos: Conteudo):
    for conteudo in conteudos:
        assert_contains(resp, conteudo.get_absolute_url())
