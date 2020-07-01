import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.django_assertions import assert_contains
from pypro.modulos.models import Modulo, Conteudo


@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)


@pytest.fixture
def conteudos(modulo):
    return mommy.make(Conteudo, 3, modulo=modulo)


@pytest.fixture
def resp(client, modulo, conteudos):
    resp = client.get(reverse('modulos:detalhe', kwargs={'slug': modulo.slug}))
    return resp


def test_titulos(resp, modulo: Modulo):
    assert_contains(resp, modulo.titulo)


def test_descricao(resp, modulo: Modulo):
    assert_contains(resp, modulo.descricao)


def test_publico(resp, modulo: Modulo):
    assert_contains(resp, modulo.publico)


def test_conteudos_titulos(resp, conteudos):
    for conteudo in conteudos:
        assert_contains(resp, conteudo.titulo)


def test_conteudos_links(resp, conteudos):
    for conteudo in conteudos:
        assert_contains(resp, conteudo.get_absolute_url())
