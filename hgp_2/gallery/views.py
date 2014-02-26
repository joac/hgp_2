from django.shortcuts import render
# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Album

def index(request):
    return for_album(request, 'home')


def for_album(request, album, page=1):
    albums =  Album.objects.filter(show_on_navbar=True).order_by('-nav_order')

    try:
        album = Album.objects.get(slug=album)
    except Album.DoesNotExist:
        return render(request, 'error.html', {'album': album})

    paginator = Paginator(album.get_all_resources(), 1)

    try:
        resources = paginator.page(page)
    except PageNotAnInteger:
        resources = paginator.page(1)
    except EmptyPage:
        resources = paginator.page(paginator.num_pages)


    res = resources[0]
    return render(request, 'index.html', {
        'albums': albums,
        'album': album,
        'res': res,
        'resources' : resources,
    })
