from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
# from django.template import loader
from .models import Album, Song


# Create your views here.
# def index(request):
#     return HttpResponse("<h3>The music app homepage</h3>")

# def index(request):
#     all_albums = Album.objects.all()
#     html = ''
#     for album in all_albums:
#         url = '/music/' + str(album.id) + '/'
#         html += '<a href="' + url + '">' + album.album_title + '</a><br>'
#     return HttpResponse(html)

# def index(request):
#     all_albums = Album.objects.all()
#     template = loader.get_template('music/index.html')
#     context = {
#         'all_albums': all_albums,
#     }
#     return HttpResponse(template.render(context, request))

def index(request):
    albums = Album.objects.all()
    context = {'albums': albums, }
    return render(request, 'music/index.html', context)


def detail(request, album_id):

    # return HttpResponse("<h2>Details for Album id:" + str(id) + "</h2>")
    # try:
    #     album = Album.objects.get(pk=album_id)
    #     context = {'album': album}
    # except Album.DoesNotExist:
    #     raise Http404("Album does not exist")

    album = get_object_or_404(Album, pk=album_id)
    context = {'album': album}
    return render(request, 'music/detail.html', context)


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        context = {
            'album': album,
            'error_message': 'You did not select any song',
        }
        return render(request, 'music/detail.html', context)
    else:
        if selected_song.is_favorite:
            selected_song.is_favorite = False
            selected_song.save()
        else:
            selected_song.is_favorite = True
            selected_song.save()

        context = {
            'album': album
        }
        return render(request, 'music/detail.html', context)
