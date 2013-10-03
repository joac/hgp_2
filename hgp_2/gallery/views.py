from django.shortcuts import render
# Create your views here.

from .models import Album

def index(request):
    return for_album(request, 'portfolio')


def for_album(request, album):
    try:
        album = Album.objects.get(name=album)
    except Album.DoesNotExist:
        return render(request, 'error.html', {'album': album})

    res = album.get_first_resource()
    print res
    return render(request, 'index.html', {
        'album': album,
        'res': res,
    })

