import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.django_assertions import assert_contains
from pypro.modulos.models import Modulo, Conteudo


@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)


@pytest.fixture
def conteudo(modulo):
    return mommy.make(Conteudo, modulo=modulo)


@pytest.fixture
def resp(client, conteudo):
    resp = client.get(reverse('modulos:conteudo', kwargs={'slug': conteudo.slug}))
    return resp


def test_titulos(resp, conteudo: Conteudo):
    assert_contains(resp, conteudo.titulo)


def test_vimeo(resp, conteudo: Conteudo):
    assert_contains(resp, f'<iframe src="https://player.vimeo.com/video/{ conteudo.vimeo_id }"')
