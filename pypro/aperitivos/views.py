from django.shortcuts import render, get_object_or_404

from pypro.aperitivos.models import Video

videos = [
    Video(slug='gato-tapa', titulo='Gato do tapa', vimeo_id='431606560'), #Titulo do video
    Video(slug='crazy-cat', titulo='Crazy cat', vimeo_id='84369192'),
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})
