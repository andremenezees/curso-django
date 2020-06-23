from django.shortcuts import render


def video(request, slug):
    video = {'titulo': 'Videos de gatos', 'vimeo_id': '431606560'}
    return render(request, 'aperitivos/video.html', context={'video': video})
