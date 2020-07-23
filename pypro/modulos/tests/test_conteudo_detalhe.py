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
def resp(client_com_usuario_logado, conteudo):
    resp = client_com_usuario_logado.get(reverse('modulos:conteudo', kwargs={'slug': conteudo.slug}))
    return resp


def test_titulos(resp, conteudo: Conteudo):
    assert_contains(resp, conteudo.titulo)


def test_vimeo(resp, conteudo: Conteudo):
    assert_contains(resp, f'<iframe src="https://player.vimeo.com/video/{ conteudo.vimeo_id }"')


def test_modulo_breadcrumb(resp, modulo: Modulo):
    assert_contains(resp, f'<li class="breadcrumb-item"><a href="{modulo.get_absolute_url()}">{modulo.titulo}</a></li>')


@pytest.fixture
def resp_usuario_nao_logado(client, conteudo):
    resp = client.get(reverse('modulos:conteudo', kwargs={'slug': conteudo.slug}))
    return resp
