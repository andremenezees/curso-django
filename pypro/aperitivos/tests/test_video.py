import pytest
from django.urls import reverse

from pypro.aperitivos.models import Video
from pypro.django_assertions import assert_contains


@pytest.fixture
def video(db):
    v = Video(slug='gato-tapa', titulo='Videos de gatos', vimeo_id='431606560') #Titulo da pagina
    v.save()
    return v


@pytest.fixture
def resp(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug,)))

@pytest.fixture
def resp_video_nao_encontrado(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug+'video_nao_existente',)))

def test_status_code_video_nao_encontrado(resp_video_nao_encontrado):
    assert resp_video_nao_encontrado.status_code == 404

def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp, video):
    assert_contains(resp, video.titulo)


def test_conteudo_video(resp, video):
    assert_contains(resp, f'<iframe src="https://player.vimeo.com/video/{video.vimeo_id}"')